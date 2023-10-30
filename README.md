# aws-sns-lambda-retry-sample

## Consumer Logs

---

| message                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| INIT_START Runtime Version: python:3.8.v31 Runtime Version ARN: arn:aws:lambda:us-east-1::runtime:05a1944859083528568a8398e5aec22be94bdaefef94faafa061158bf4530956                               |
| START RequestId: 2cfa6d4c-a5e1-4644-a04e-5cd98d6cc8bb Version: $LATEST                                                                                                                           |
| Timestamp for MessageId 'd5c2ca36-c56d-4a52-b16e-70989515632c': 2023-10-30T15:36:41.642054                                                                                                       |
| Successfull run for message with ID: d5c2ca36-c56d-4a52-b16e-70989515632c                                                                                                                        |
| END RequestId: 2cfa6d4c-a5e1-4644-a04e-5cd98d6cc8bb                                                                                                                                              |
| REPORT RequestId: 2cfa6d4c-a5e1-4644-a04e-5cd98d6cc8bb Duration: 3.04 ms Billed Duration: 4 ms Memory Size: 1024 MB Max Memory Used: 38 MB Init Duration: 158.38 ms                              |
| START RequestId: 2ae06306-26f7-4398-8937-ede9404f9a21 Version: $LATEST                                                                                                                           |
| Timestamp for MessageId '548a659a-48aa-4172-bff0-8a45a4c7e995': 2023-10-30T15:37:47.439920                                                                                                       |
| [ERROR] Exception: Random error for testing retry! Traceback (most recent call last):   File "/var/task/consumer.py", line 21, in handler     raise Exception("Random error for testing retry!") |
| END RequestId: 2ae06306-26f7-4398-8937-ede9404f9a21                                                                                                                                              |
| REPORT RequestId: 2ae06306-26f7-4398-8937-ede9404f9a21 Duration: 2.80 ms Billed Duration: 3 ms Memory Size: 1024 MB Max Memory Used: 39 MB                                                       |
| START RequestId: 2ae06306-26f7-4398-8937-ede9404f9a21 Version: $LATEST                                                                                                                           |
| Timestamp for MessageId '548a659a-48aa-4172-bff0-8a45a4c7e995': 2023-10-30T15:38:45.617455                                                                                                       |
| Successfull run for message with ID: 548a659a-48aa-4172-bff0-8a45a4c7e995                                                                                                                        |
| END RequestId: 2ae06306-26f7-4398-8937-ede9404f9a21                                                                                                                                              |
| REPORT RequestId: 2ae06306-26f7-4398-8937-ede9404f9a21 Duration: 1.53 ms Billed Duration: 2 ms Memory Size: 1024 MB Max Memory Used: 39 MB                                                       |

---
