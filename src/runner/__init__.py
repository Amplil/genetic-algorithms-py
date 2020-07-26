class Runner:
    """
    Description:
    ------------
    実行ヘルパー
    """

    def __init__(self, algorithm):
        self.__algorithm = algorithm
        self.__main()

    def __main(self):
        while not self.__algorithm.has_reached:
            self.__algorithm.step()
