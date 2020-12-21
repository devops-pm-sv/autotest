# encoding: utf-8
# @Time    : 2020/12/4 11:28
# @Author  : zhoubo
# @dsc     :
import xlrd

class ReadExcel():
    """读取excel数据"""
    def __init__(self,fileName, SheetName="Sheet1"):
        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_name(SheetName)
        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols


    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listData.append(api_dict)
            return listData
        else:
            print("表格无数据")
            return None


if __name__ == '__main__':
    file = "C:\\Users\BBD\Desktop\守信红名单.xlsx"
    e = ReadExcel(file,"工作表1")
    r = e.read_data()
    print(r)




