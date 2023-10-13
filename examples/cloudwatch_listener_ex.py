from locust import main, events
from locust_plugins.listeners.cloudwatch import CloudwatchAdapter, ServiceContext
from locust_plugins import missing_extra

try:
    import boto3
except ModuleNotFoundError:
    missing_extra("boto3", "boto3")


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    CloudwatchAdapter(boto3.client("cloudwatch"), environment, ServiceContext("MyExampleService", "perf"))


if __name__ == "__main__":
    main.main()