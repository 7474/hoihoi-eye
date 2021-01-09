# hoihoi eye

[ホイホイさんのプラモデル](https://www.kotobukiya.co.jp/product/product-0000003489/)に組み込んだカメラをRaspberry Pi Zeroで処理するためのスクリプトです。

## ハードウェア

- Raspberry Pi
    - Raspberry Pi Zero WH
- カメラ
    - [YMaxラズベリーパイゼロ用広角カメラモジュール](https://www.amazon.co.jp/gp/product/B083GRBLP5/)
- ディスプレイ
    - [物理解像度240x240、論理解像度480x480のもの](http://www.spotpear.com/index/product/detail/id/70.html)
- ホイホイさん
    - [ホイホイさん NEW EDITION](https://www.kotobukiya.co.jp/product/product-0000003489)

## 依存関係

```sh
wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv6l.whl
pip3 install tensorflow-2.4.0-cp37-none-linux_armv6l.whl
sudo apt install fonts-noto-cjk
```

## 実行

```sh
# 学習済モデルのダウンロード
bash download.sh /tmp
# ダウンロードしたモデルを指定して実行
python3 detect_picamera.py \
  --model /tmp/detect.tflite \
  --labels /tmp/coco_labels.txt
```

## Thanks

このリポジトリは[TenorFlowのサンプル](https://github.com/tensorflow/examples/tree/9241dd1f44c503a95e540c85f5084e805bca6028/lite/examples/object_detection/raspberry_pi)を元にしました。
