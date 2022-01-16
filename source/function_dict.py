class HEZdict:
    """
    ver: 1.1.0\n
    입력값과 기준(=칼럼)을 바탕으로 어휘를 검색하고
    검색된 어휘를 사전처럼 나열.\n
    """
    def __init__(self, df):
        self.df = df

    def findword_exact(self, resultList, criterion, exact_param):
        """
        ver: 1.1.0\n
        @param resultList: 이름은 리스트지만 단순히 검색할 문자열입니다.\n
        @param criterion: 숫자로 입력된 검색 칼럼 제목입니다. 자세한 사항은 transCriterion 참고.
        """
        
        criterion = self.transCriterion(criterion)
        resultNumList = []
        
        if int(exact_param) == 0:
            for i in range(len(self.df[criterion])):
                if self.df.loc[i, criterion] == resultList:
                    resultNumList.append(i)
        elif int(exact_param) == 1:
            for i in range(len(self.df[criterion])):
                if resultList in self.df.loc[i, criterion]:
                    resultNumList.append(i)

        return resultNumList

    def transCriterion(self, criterion):
        if criterion == '0':
            criterion = '전사(변환)'
        elif criterion == '1':
            criterion = '출전'
        elif criterion == '2':
            criterion = '한어'
        elif criterion == '3':
            criterion = '한국어'
        else:
            print("Warning: Invalid Input")
            return

        return criterion