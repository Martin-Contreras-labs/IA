from rxthorax.pipelines.first_delivery import FirstDeliveryPipeline


def main() -> None:
    pipeline = FirstDeliveryPipeline.from_default_config()
    print(pipeline.describe())


if __name__ == "__main__":
    main()
