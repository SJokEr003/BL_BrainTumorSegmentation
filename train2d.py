# -*- coding: utf-8 -*-
#
# @Date    : 2018/7/16
# @Author  : Bin LIN
# Copyright (c) 2017-2018 University of St. Andrews, UK. All rights reserved
#

import argparse
import json
import tensorflow as tf
from ResNet2D import ResnetBuilder
from vgg16 import vgg_model
import vgg16
import UNet
from load_data_2d import ScanReader
from keras.utils import to_categorical
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

n_classes = 4
BATCH_SIZE = 4
TRAINING_DATA_DIRECTORY = 'MICCAI_BraTS_2018_Data_Training'
INPUT_SIZE = '240, 155'
LEARNING_RATE = 1e-4
NUM_STEPS = 20000
RESTORE_FROM = './deeplab_resnet.ckpt'
SAVE_NUM_IMAGES = 2
SAVE_PRED_EVERY = 100
SNAPSHOT_DIR = './snapshots/'


def get_arguments():
    parser = argparse.ArgumentParser(description='ResNet')
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE,
                        help='Number of scans sent to network in one step.')
    parser.add_argument("--data-dir", type=str, default=TRAINING_DATA_DIRECTORY, help='Path to BraTS2018 training set.')
    parser.add_argument("--input-size", type=str, default=INPUT_SIZE,
                        help='Comma-separated string with height and width of images')
    parser.add_argument("--is-training", action='store_true',
                        help='Wether to update the running means and variances during training')
    parser.add_argument("--learning-rate", type=float, default=LEARNING_RATE, help='Learning rate for training')
    parser.add_argument("--num-steps", type=int, default=NUM_STEPS, help='Number of training steps')
    parser.add_argument("--random-scale", action='store_true',
                        help='Whether to randomly scale the inputs during training')
    parser.add_argument("--restore-from", type=str, default=RESTORE_FROM, help="Where restore model parameters from.")
    parser.add_argument("--save-num-images", type=int, default=SAVE_NUM_IMAGES, help="How many images to save.")
    parser.add_argument("--save-pred-every", type=int, default=SAVE_PRED_EVERY,
                        help="Save summaries and checkpoint every often.")
    parser.add_argument("--snapshot-dir", type=str, default=SNAPSHOT_DIR, help="Where to save snapshots of the model.")

    return parser.parse_args()


def load_data():
    args = get_arguments()
    scan_reader = ScanReader(args.data_dir)
    scans, labels = scan_reader.scan_img, scan_reader.label_img
    print(scans)
    print(labels)


def main():
    # l = np.random.randint(10, size=(1000, 1))
    # print(l)
    # print(l.shape)
    # one_hot_l = to_categorical(l, num_classes=10)
    # print(one_hot_l)
    # exit(0)
    # Build ResNet-101 model
    model = ResnetBuilder.build_resnet_101((240, 155, 1), 1)
    # unet = UNet.UNet3D((240, 240, 155, 1))
    # vgg_model = vgg16.vgg_model()
    print("Model Built")

    # Compiling
    # model.compile(loss="categorical_crossentropy", optimizer="sgd")
    model.compile(loss="binary_crossentropy", optimizer="sgd")
    # unet.compile(loss="categorical_crossentropy", optimizer="sgd")
    # vgg_model.compile(loss="categorical_crossentropy", optimizer="sgd")
    print("Done compiling")
    print("model input shape", model.input_shape)
    print("model output shape", model.output_shape)
    # print(unet.input_shape)
    # print(unet.output_shape)
    # print("vgg", vgg_model.input_shape)
    # print("vgg", vgg_model.output_shape)
    # exit(0)
    # labels = labels.squeeze()

    args = get_arguments()
    scan_reader = ScanReader(args.data_dir)
    # Get input and output
    # scans = [samples, channels, depth, height, width]
    # labels = [samples, depth, height, width]
    scans, labels = scan_reader.scan_img, scan_reader.label_img
    # validation_scans, validation_labels = scan_reader.validation_scans, scan_reader.validation_labels
    # Reshape input to fit Tensorflow backend
    # [samples, depth, height, width, channel]
    # print(type(scans))
    scans = np.expand_dims(np.array(scans), -1)
    # print(scans.shape)
    with open("whole_tumor_label.json", "r") as f:
        try:
            while True:
                line = f.readline()
                if line:
                    split_dict = line.split('}')
                    for dict_str in split_dict:
                        line = dict_str + '}'
                        patient_dict = json.loads(line)
                        print(patient_dict.keys())
                else:
                    break
        except:
            f.close()
    exit(0)
    label = []
    for key in l:
        label = [w for (_, w) in l[key]]

    labs = label + label
    labs = labs + label
    labs = labs + label
    # print(len(labs))
    label = np.array(labs)
    label = np.reshape(label, (960,))
    # print(label)
    print(label.shape)
    # labels = np.expand_dims(np.array(labels), -1)
    # labels = np.expand_dims(np.array(labels), 0)
    # scans = tf.expand_dims(scans, -1)
    # labels = tf.expand_dims(labels, -1)
    # validation_scans = tf.expand_dims(validation_scans, -1)
    # validation_labels = tf.expand_dims(validation_labels, -1)
    # print(scans.shape)
    # print(labels.shape)
    # print(validation_scans)
    # print(validation_labels)
    # exit(0)

    labels_binary = []
    row_binary = []
    # for l in labels:
    #     print(l.shape)
    #     onehot = to_categorical(l, num_classes=5)
    #     print(onehot)
    #     print(onehot.shape)
    #     exit(0)
    #     labels_binary.append(onehot)
    # for row in l:
    #     row = to_categorical(row, 5)
    #     row_binary.append(row)
    # labels_binary.append(row_binary)
    # row_binary = []
    # print(labels_binary[60])
    # labels_binary = np.array(labels_binary)
    # labels_binary = to_categorical(labels, num_classes=5)
    # print(labels_binary[84][90])
    # print(labels_binary.shape)
    # exit(0)
    # class_label = np.random.randint(5, size=(5, 5))

    # onehot_labels = to_categorical(label, num_classes=2)
    # onehot_labels = np.expand_dims(onehot_labels, 0)
    # print(type(onehot_labels))
    # print(class_label)
    # print(onehot_labels[58])
    # print(len(onehot_labels))
    # print(onehot_labels.shape)
    # exit(0)
    model.fit(scans, label, epochs=10)
    # model.fit(scans, labels_binary, epochs=10, steps_per_epoch=1000)
    # model.fit(scans, onehot_labels, epochs=10, steps_per_epoch=1000)
    # print("Done training")
    # prediction = model.predict(validation_scans)
    # print(prediction.shape())
    # print(len(prediction))


if __name__ == '__main__':
    main()
