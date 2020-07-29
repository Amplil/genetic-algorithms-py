from target import ITarget
from ..interfaces import IContext, IFunctionSet, IPhenotype


class Context(IContext):
    """
    Description:
    ------------
    コンテキスト
    """

    __target: ITarget
    __current: int
    __node_count: int
    __functions: IFunctionSet
    __phenotype: IPhenotype
    __action_frame: int

    def __init__(self, target: ITarget, start: int, node_count: int, functions: IFunctionSet, phenotype: IPhenotype) -> None:
        self.__target = target
        self.__current = start
        self.__node_count = node_count
        self.__functions = functions
        self.__phenotype = phenotype
        self.__action_frame = target.settings.action_frame
        self.__skip = 0

    @property
    def target(self) -> ITarget:
        return self.__target

    @property
    def current(self) -> int:
        return self.__current

    @current.setter
    def current(self, current: int) -> None:
        self.__current = current

    @property
    def node_count(self) -> int:
        return self.__node_count

    @property
    def functions(self) -> IFunctionSet:
        return self.__functions

    @property
    def phenotype(self) -> IPhenotype:
        return self.__phenotype

    @property
    def is_skipping_frame(self) -> bool:
        if self.__action_frame <= 1:
            return False

        self.__skip += 1
        if self.__skip >= self.__action_frame:
            self.__skip = 0
            return False
        return True
