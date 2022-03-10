# 公   司：峦锘科技
# 作   者：潘浩
# 创建时间：2022/3/10 14:29
# 备   注：无
def show(nums={}):
    print('+-----------+-----------+-----------+-----------+-----------+-----------+')
    print('|\t行 号\t|\t座位1\t|\t座位2\t|\t座位3\t|\t座位4\t|\t座位5\t|')
    print('+-----------+-----------+-----------+-----------+-----------+-----------+')
    for i in range(15):
        print('|\t第{0}行'.format(i+1), end='\t|')
        for j in range(5):
            print('\t{0}\t'.format('已售' if len(nums) > 0 and nums.get(i+1) and j+1 in nums.get(i+1) else '有座'), end='\t|')
        print()
    print('+-----------+-----------+-----------+-----------+-----------+-----------+')
def buy():

    solds = {}
    while True:
        go = input('请输入座位号：')
        if go:
            if go == 'n' or go == 'N':
                count = 0
                for i in solds:
                    count += len(solds.get(i))
                print('谢谢使用，本次购票共{0}张'.format(count))
                break
        nums = go.split(',')
        if solds.get(int(nums[0])):
            solds[int(nums[0])].append(int(nums[1]))
        else:
            solds[int(nums[0])] = [int(nums[1])]
        show(solds)
if __name__ == '__main__':
    show()
    buy()