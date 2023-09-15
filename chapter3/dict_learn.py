# dict
# 1. 字典推导式
def dict_generate():
    dial_codes = [(880, 'Bangladesh'), (55, 'Brazil'), (86, 'China'), ]
    # 转换为country为key, code为value的dict; 通过遍历dial_codes
    country_dial = {country: code
                    for code, country in dial_codes}
    print(country_dial)
    cd = {code: country.upper()
          for country, code in sorted(country_dial.items())
          if code < 90}
    print(cd)

if __name__ == '__main__':
    dict_generate()