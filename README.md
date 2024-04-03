# YandexDiskSync
Short scripts to sync your dirs with YandexDisk

You can push directories to the cloud and pull them up from there, using YandexAPI.

### Install
To install you should clone this repo and run next command:
```bash
chmod u+x install.sh
chmod u+x yadisk.sh
./install.sh
```

Also You need to get OAuth-token from [link](https://yandex.ru/dev/disk-api/doc/ru/concepts/quickstart#quickstart__oauth)

### Usage

To use run next next command:
```bash
./yadisk.sh [action] [dirName]
```
- [action] - push or pull

- [dirName] - name of the folder for the action

### Libs
- [YaDisk](https://pypi.org/project/yadisk/)
- [Requests](https://pypi.org/project/requests/)