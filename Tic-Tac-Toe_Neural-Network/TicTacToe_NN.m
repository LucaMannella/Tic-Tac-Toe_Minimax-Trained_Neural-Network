clear all
close all
clc

disp('      __                     _       __     _                      _     ')
disp('   /\ \ \___ _   _ _ __ __ _| |   /\ \ \___| |___      _____  _ __| | __ ')
disp('  /  \/ / _ \ | | |  __/ _` | |  /  \/ / _ \ __\ \ /\ / / _ \|  __| |/ / ')
disp(' / /\  /  __/ |_| | | | (_| | | / /\  /  __/ |_ \ V  V / (_) | |  |   <  ')
disp(' \_\ \/ \___|\__,_|_|  \__,_|_| \_\ \/ \___|\__| \_/\_/ \___/|_|  |_|\_\ ')
disp('  Developed by Luca Mannella - August 2017                     (!) v0.5  ')
disp('                                                                         ')

load('..\files\nn_input.txt')
load('..\files\nn_output.txt')

inputs = nn_input';
targets = nn_output';

%% Training, validating, testing = [60, 0, 40]
trainingPerc = 60/100;
validatingPerc = 0;
testingPerc = 40/100;

disp('Training: 60/100 - Testing: 40/100')
NN_Train_Test(length(targets), inputs, targets, trainingPerc, validatingPerc, testingPerc)

%% Training, validating, testing = [50, 10, 40]
trainingPerc = 50/100;
validatingPerc = 10/100;
testingPerc = 40/100;

disp('Training: 50/100 - Validating: 10/100 - Testing: 40/100')
NN_Train_Test(length(targets), inputs, targets, trainingPerc, validatingPerc, testingPerc)

%% Training, validating, testing = [70, 15, 15]
trainingPerc = 70/100;
validatingPerc = 15/100;
testingPerc = 15/100;

disp('Training: 70/100 - Validating: 15/100 - Testing: 15/100')
NN_Train_Test(length(targets), inputs, targets, trainingPerc, validatingPerc, testingPerc)

%% Training, validating, testing = [90, 0, 10]
trainingPerc = 90/100;
validatingPerc = 0;
testingPerc = 10/100;

disp('Training: 90/100 - Testing: 10/100')
NN_Train_Test(length(targets), inputs, targets, trainingPerc, validatingPerc, testingPerc)