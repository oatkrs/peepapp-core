# 🌟 **PeepApp Core** 🌟
Welcome to **PeepApp Core** – the heart of your app security journey! 🔐 This core library powers **PeepApp**, your go-to tool for performing SAST (Static Application Security Testing) on Android apps. Whether you're diving into an APK or analyzing a Google Play Store link, **PeepApp** has you covered, helping you uncover hidden trackers and permissions! 🚨

## 🚀 **Features** 🚀
✨ **Static Analysis** – Dissect those APKs with precision!  
🔍 **Network Analysis** – Peek into app communications!  
🌐 **Connection Helper** – Smooth connections, streamlined processes!

## 📦 **Installation** 📦
Get started in a snap! **PeepApp Core** is just a pip away! 🐍

```shell
pip install peepapp-core
```

## 🛠️ **Include in Your Project** 🛠️
Easily integrate **PeepApp Core** by adding it to your `requirements.txt`. Just replace 'XX' with your desired subversion:

```text
peepapp-core==XX
```

## 💻 **Local Usage** 💻
Ready to roll up your sleeves? Follow these steps to get started locally! 💪

### 1️⃣ **Clone the Repository** 🧬
Get your hands on the code:

```shell
git clone https://github.com/oatkrs/peepapp-core.git
cd peepapp-core
```

### 2️⃣ **Using Docker? We've Got You!** 🐳
Spin up a Docker container in no time:

```shell
docker build -t peepapp-core .
```

Run tests with ease:

```shell
docker run -it --rm peepapp-core /bin/bash
python -m unittest discover -s peepapp_core -p "test_*.py"
```

### 3️⃣ **Prefer Manual Installation? No Problem!** 🔧
Start by installing `dexdump`:

```shell
sudo apt-get install dexdump
```

Set up a Python `virtualenv`:

```shell
virtualenv venv -p python3
source venv/bin/activate
```

Install all dependencies:

```shell
pip install -r requirements.txt
```

Run the tests:

```shell
python -m unittest discover -s peepapp_core -p "test_*.py"
```

---

Dive in, and let's make app security and user privacy a breeze! 🛡️