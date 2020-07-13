from models import CarBrand
from models import CarModelFamily
from models import CarModel
from models import CarObject
from database import db_session
import saver.main_saver
from sqlalchemy.sql import select
from sqlalchemy.sql import and_, or_, not_
import datetime
import sys


class Global:

    def run_b_f(self):
        brand_saver = saver.main_saver.BrandSaver()
        brand_saver.save({})
        for item in brand_saver.get_items():
            family_saver = saver.main_saver.FamilySaver()
            family_saver.save({
                'brand_oid': item['id']
            })
            print(f'families for brand {item["id"]} processed')

    def run_c_m(self):
        i = 1
        for item in db_session.query(CarModelFamily):
            model_saver = saver.main_saver.ModelSaver()
            model_saver.save({
                'brand_oid': item.brand_id,
                'family_oid': item.id,
            })
            print(f'#{i} models for family {item.id} processed')
            i += 1

    def run_c_o(self):
        for item in db_session.query(CarBrand, CarModelFamily, CarModel).filter(
                CarModelFamily.id == CarModel.family_id,
                CarBrand.id == CarModelFamily.brand_id
        ):
            object_saver = saver.main_saver.ObjectSaver()
            object_saver.save({
                'brand_id': item[0].id,
                'family_id': item[1].id,
                'model_id': item[2].id}
            )
            print(f'combination {item[0].id} {item[1].id} {item[2].id} processed')

    def run_p_o(self):
        i = 1
        for item in db_session.query(CarObject).filter(CarObject.id > 1998):
            object_saver = saver.main_saver.ProductSaver()
            object_saver.set_object_id(item.id)
            object_saver.save({
                'filter_by_car[brand_oid]': item.brand_id,
                'filter_by_car[family_oid]': item.family_id,
                'filter_by_car[model_oid]': item.model_id
            })
            print(f'#{i} products for combination {item.id} saved')
            i += 1


if __name__ == '__main__':
    option = sys.argv[1] if len(sys.argv) > 1 else ''
    global_c = Global()
    if option == 'brand' or option == 'all':
        print('--Brands & Families --')
        global_c.run_b_f()

    if option == 'model' or option == 'all':
        print('--Models--')
        global_c.run_c_m()

    if option == 'object' or option == 'all':
        print('--CarObjects--')
        global_c.run_c_o()

    if option == 'item' or option == 'all':
        print('--Items--')
        global_c.run_p_o()

    if option == '':
        print('Nothing choose')
