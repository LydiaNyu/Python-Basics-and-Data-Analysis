# Part 1 goes here!
class DecodeError(Exception):
    pass
class ChunkError(Exception):
    pass
class BitList:
    def __init__(self, value):
        for i in value：
            if (i != '0' and i != '1'):
                raise ValueError('Format is invalid; does not consist of only 0 and 1')
        theList = []
        for n in value:
            theList.append(int(n))
        self.value = theList

    @staticmethod
    def from_ints(*args):
        aList = []
        for i in args:
            if (i != 0 and i != 1):
                raise ValueError('Format is invalid; does not consist of only 0 and 1')
        for n in args:
            aList.append(n)
        aBitList = BitList('0')
        aBitList.value = aList
        return aBitList

    def __eq__(self, other):
        a = self.value
        b = other.value
        if len(a)!= len(b):
            return False
        for i in range(len(a)):
            if(a[i]!=b[i]):
                return False
        return True

    def __str__(self):
        k = ''
        for i in self.value:
            k += str(i)
        return k

    def arithmetic_shift_left(self):
        k = []
        for i in range(1,len(self.value)):
            k.append(self.value[i])
        k.append(0)
        self.value = k

    def arithmetic_shift_right(self):
        k = []
        k.append(self.value[0])
        k.append(self.value[0])
        for i in range(1,len(self.value)-1):
            k.append(self.value[i])
        self.value = k

    def bitwise_and(self,other):
        a = self.value
        b = other.value
        aList = []
        if len(a) != len(b):
            raise ValueError('Format is invalid; the length of value of two instances should be same')
        for i in range(len(a)):
            if(a[i]==1 and b[i]==1):
                aList.append(1)
            else:
                aList.append(0)
        aBitList = BitList('0')
        aBitList.value = aList
        return aBitList

    def chunk(self, aInt):
        if ((len(self.value) % aInt) != 0):
            raise ChunkError("it could not be divided to subgroups with equal length of {}".format(aInt))
        k = len(self.value) // aInt
        finalList = []
        count = 0
        for i in range(k):
            aList = []
            for z in range(aInt):
                aList.append(self.value[count])
                count += 1
            finalList.append(aList)
        return finalList

    def decode(self, encoding='utf-8'):
        if (encoding != 'us-ascii' and encoding != 'utf-8'):
            raise ValueError("the encoding is not supported")
        f = self.value
        s = ''
        if (encoding == 'us-ascii'):
            count = 0
            while count < len(f):
                d = ''
                if (count < len(f) - 7):
                    for i in range(7):
                        d = d + str(f[count])
                        count += 1
                else:
                    for i in range(len(f) - count):
                        d = d + str(f[count])
                        count += 1
                deciNum = int(d, 2)
                s = s + chr(deciNum)
            return s

        if (encoding == 'utf-8'):
            count = 0
            while count < len(f):
                d = ''
                if (f[count] == 0):
                    for n in range(8):
                        d = d + str(f[count])
                        count += 1
                    deciNum = int(d, 2)
                    s = s + chr(deciNum)
                elif (f[count] == 1):
                    count += 1
                    if (f[count] == 0):
                        raise DecodeError('an invalid leading byte')
                    count += 1
                    if (f[count] == 0):
                        count += 1
                        for n in range(5):
                            d = d + str(f[count])
                            count += 1
                        if(f[count] != 1 or f[count+1] != 0):
                            raise DecodeError('an invalid continuaton byte')
                        count += 2
                        for n in range(6):
                            d = d + str(f[count])
                            count += 1
                        deciNum = int(d, 2)
                        s = s + chr(deciNum)
                    elif (f[count] == 1):
                        count += 1
                        if (f[count] == 0):
                            print(count)
                            count += 1
                            for n in range(4):
                                d = d + str(f[count])
                                count += 1
                            for k in range(2):
                                if (f[count] != 1 or f[count + 1] != 0):
                                    raise DecodeError('an invalid continuaton byte')
                                count += 2
                                for j in range(6):
                                    d = d + str(f[count])
                                    count += 1
                            deciNum = int(d, 2)
                            s = s + chr(deciNum)
                            print(count)
                        elif (f[count] == 1):
                            count += 1
                            for n in range(4):
                                d = d + str(f[count])
                                count += 1
                            for n in range(3):
                                if (f[count] != 1 or f[count + 1] != 0):
                                    raise DecodeError('an invalid continuaton byte')
                                count += 2
                                for n in range(6):
                                    d = d + str(f[count])
                                    count += 1
                            deciNum = int(d, 2)
                            s = s + chr(deciNum)
                            print(count)
            return s
# 




















