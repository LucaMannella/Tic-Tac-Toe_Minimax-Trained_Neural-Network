clear all
close all
clc

disp('      __                     _       __     _                      _     ')
disp('   /\ \ \___ _   _ _ __ __ _| |   /\ \ \___| |___      _____  _ __| | __ ')
disp('  /  \/ / _ \ | | |  __/ _` | |  /  \/ / _ \ __\ \ /\ / / _ \|  __| |/ / ')
disp(' / /\  /  __/ |_| | | | (_| | | / /\  /  __/ |_ \ V  V / (_) | |  |   <  ')
disp(' \_\ \/ \___|\__,_|_|  \__,_|_| \_\ \/ \___|\__| \_/\_/ \___/|_|  |_|\_\ ')
disp('  Developed by Luca Mannella - August 2017            (!) v0.4 - manual  ')
disp('                                                                         ')

load('..\files\nn_input.txt')
load('..\files\nn_output.txt')


%% 50 hidden neurons
[outputs50, errors50, performance50, nRightValues50, rightValuesPerc50] = NeuralNetworkManual(nn_input, nn_output, 50, 60/100, false);

disp('Number of correct values using 50 neurons in the hidden layer')
nRightValues50
performance50


%% 120 hidden neurons
[outputs120, errors120, performance120, nRightValues120, rightValuesPerc120] = NeuralNetworkManual(nn_input, nn_output, 120, 60/100, false);

disp('Number of correct values using 120 neurons in the hidden layer')
nRightValues120
performance120


%% 500 hidden neurons
[outputs500, errors500, performance500, nRightValues500, rightValuesPerc500] = NeuralNetworkManual(nn_input, nn_output, 500, 60/100, false);

disp('Number of correct values using 500 neurons in the hidden layer')
nRightValues500
performance500


%% 1000 hidden neurons
[outputs1000, errors1000, performance1000, nRightValues1000, rightValuesPerc1000] = NeuralNetworkManual(nn_input, nn_output, 1000, 60/100, false);

disp('Number of correct values using 1000 neurons in the hidden layer')
nRightValues1000
performance1000


