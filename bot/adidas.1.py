#Base URL + https://www.adidas.com/us/ultraboost-parley-shoes/AC7836_580.html?forceSelSize=AC7836_580

def URLGen(model, size):
    BaseSize = 580
    #Base size is for Shoe Size 6.5
    ShoeSize = size - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize * BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
    return URL
Model = raw_input('Model #')
Size = input ('Size: ')

URL = URLGen(Model, Size)

print(str(URL))
