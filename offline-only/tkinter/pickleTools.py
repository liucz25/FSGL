import pickle
def psave(data,file="data.bin"):
    with open(file, 'wb') as f:
        pickle.dump(data, f)

    # print("ok")


def pload(file="data.bin"):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

if __name__ == '__main__':
    a={}
    b=[2313,32,1,3,4]
    a['c']=b
    psave(a)
    d=pload()
    print(d)

