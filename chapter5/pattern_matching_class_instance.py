# 模式匹配实例
import typing


# 1.简单类模式
def simple_class_pattern(tar):
    match tar:
        case float():
            print(f'tar is {tar:.2f}')
        case str():
            print(f'tar is string, value is {tar}')
            # float(lat) 这种只适用于9中内置类型, bytes, dict, float, frozenset, int, list, set, str, tuple
        case [str(name), _, _, (float(lat)), (float(lon))]:
            print(f'name is {name}, lat is {lat}, lon is {lon}')
        case _:
            print(f'No match')

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str

# 2. 关键字类模式
def keywords_class_pattern():
    cites = [City('Asia', 'Tokyo', 'JP'),
             City('North America', 'New York', 'US'),
             City('South America', 'Sao Paulo', 'BR'),
             City('Asia', 'BeiJing', 'CN'),]
    for city in cites:
        match city:
            case City(continent='Asia', name='BeiJing', country=cc):
                print(f'来自神秘的大国, 它就是{cc}')
            case City('Asia'):
                print(f'Asia country is {city.name}')
            case _:
                print('No match')


def location_class_pattern():
    """
        想要使用位置模式, 需要有一个名为__match_args__的特殊类属性;
        其中__match_args__列出的是可供匹配的实例属性, 不是全部属性;
    """
    print(City.__match_args__)
    cites = [City('Asia', 'Tokyo', 'JP'),
             City('North America', 'New York', 'US'),
             City('South America', 'Sao Paulo', 'BR'),
             City('Asia', 'BeiJing', 'CN'), ]
    for city in cites:
        match city:
            case City(continent='Asia', name='BeiJing', country=cc):
                print(f'来自神秘的大国, 它就是{cc}')
            case City('Asia', _, country):
                print(f'_, Asia country is {country}')
            case _:
                print('No match')

if __name__ == '__main__':
    # simple_class_pattern(8.9)
    # simple_class_pattern(['hello', 2, 3, 3.1, 3.2,])
    # keywords_class_pattern()
    location_class_pattern()