from rxthorax.pipelines.h1_pipeline import H1Pipeline


def main() -> None:
    pipeline = H1Pipeline.from_default_config()
    print(pipeline.describe())


if __name__ == "__main__":
    main()
