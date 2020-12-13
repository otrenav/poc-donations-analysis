
from config import CONFIG
from printer import print_header
from describer import describe
from forecaster import forecast
from predicter import predict
from reporter import report
from loader import load
from tester import test


def main():
    print_header("START", CONFIG, level=0)
    data = load(CONFIG)

    print(data.head())
    data.to_csv("./outputs/data.csv", index=False)

    describe(data, CONFIG)
    test(data, CONFIG)
    forecast(data, CONFIG)
    predict(data, CONFIG)
    report(data, CONFIG)
    print_header("DONE", CONFIG, level=0)


if __name__ == "__main__":
    main()
