from abc import ABC, abstractmethod


class Interface(ABC):
    @staticmethod
    @abstractmethod
    def approximation_graph(x0, y0, iterations, h):
        pass

    @staticmethod
    @abstractmethod
    def error_graph(x0, y0, iterations, h):
        pass

    @staticmethod
    @abstractmethod
    def error_analysis_graph(x0, y0, X, n0, n):
        pass


def f(x, y):
    return 4 / (x ** 2) - y / x - y ** 2


class ExactSolution:
    @staticmethod
    def function(x, x0, y0):
        c = (x0 ** 4) * (4 / (x0 * y0 + 2) - 1)
        return -2 / x + 4 * (x ** 3) / (x ** 4 + c)


class EulerMethod(Interface):
    @staticmethod
    def approximation_graph(x0, y0, iterations, h):
        ret = []
        curX = x0
        curY = y0
        for _ in range(iterations):
            ret.append(curY)
            curX, curY = curX + h, curY + h * f(curX, curY)
        return ret

    @staticmethod
    def error_graph(x0, y0, iterations, h):
        ret = EulerMethod.approximation_graph(x0, y0, iterations, h)
        ret = [abs(ret[i] - ExactSolution.function(x0 + h * i, x0, y0)) for i in range(len(ret))]
        return ret

    @staticmethod
    def error_analysis_graph(x0, y0, X, n0, n):
        ret = []
        for i in range(n0, n + 1):
            h = (X - x0) / i
            ret.append(max(EulerMethod.error_graph(x0, y0, i + 1, h)))
        return ret


class ImprovedEulerMethod(Interface):
    @staticmethod
    def approximation_graph(x0, y0, iterations, h):
        ret = []
        curX = x0
        curY = y0
        for _ in range(iterations):
            ret.append(curY)
            curX, curY = curX + h, curY + h * (f(curX, curY) + f(curX + h, curY + h * f(curX, curY))) / 2
        return ret

    @staticmethod
    def error_graph(x0, y0, iterations, h):
        ret = ImprovedEulerMethod.approximation_graph(x0, y0, iterations, h)
        ret = [abs(ret[i] - ExactSolution.function(x0 + h * i, x0, y0)) for i in range(len(ret))]
        return ret

    @staticmethod
    def error_analysis_graph(x0, y0, X, n0, n):
        ret = []
        for i in range(n0, n + 1):
            h = (X - x0) / i
            ret.append(max(ImprovedEulerMethod.error_graph(x0, y0, i + 1, h)))
        return ret


class RungeKuttaMethod(Interface):
    @staticmethod
    def approximation_graph(x0, y0, iterations, h):
        ret = []
        curX = x0
        curY = y0
        for _ in range(iterations):
            ret.append(curY)
            k1 = f(curX, curY)
            k2 = f(curX + h / 2, curY + h * k1 / 2)
            k3 = f(curX + h / 2, curY + h * k2 / 2)
            k4 = f(curX + h, curY + h * k3)
            curX, curY = curX + h, curY + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return ret

    @staticmethod
    def error_graph(x0, y0, iterations, h):
        ret = RungeKuttaMethod.approximation_graph(x0, y0, iterations, h)
        ret = [abs(ret[i] - ExactSolution.function(x0 + h * i, x0, y0)) for i in range(len(ret))]
        return ret

    @staticmethod
    def error_analysis_graph(x0, y0, X, n0, n):
        ret = []
        for i in range(n0, n + 1):
            h = (X - x0) / i
            ret.append(max(RungeKuttaMethod.error_graph(x0, y0, i + 1, h)))
        return ret
