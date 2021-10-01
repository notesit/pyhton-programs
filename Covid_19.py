from covid import Covid
from translate import Translator
trans= Translator(to_lang='Marathi')

covid=Covid()
def Covid_worldwide():
    print(trans.translate(f"Total Number of active cases in world are {covid.get_total_active_cases()}"))
    print('Total confirmed cases in world are :',covid.get_total_confirmed_cases())
    print('Total recoverd cases are :',covid.get_total_recovered())
    print(trans.translate('Total number of Deaths are : '),covid.get_total_deaths())

def countryinfo(country):
    country=covid.get_status_by_country_name(country)

    # print(country)
    data={
        key : country[key]
        for key in country.keys() and {'confirmed',
                                       'active',
                                       'deaths',
                                       'recovered'}
    }
    for key , value in data.items():
        print(key ,": ", value)

    # print(data)


print(trans.translate("information of covid19 "))
Covid_worldwide()
country=input(trans.translate("Enter your country name : "))
countryinfo(country)
