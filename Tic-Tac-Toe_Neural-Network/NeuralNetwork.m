clear all
close all
clc

disp('      __                     _       __     _                      _     ')
disp('   /\ \ \___ _   _ _ __ __ _| |   /\ \ \___| |___      _____  _ __| | __ ')
disp('  /  \/ / _ \ | | |  __/ _` | |  /  \/ / _ \ __\ \ /\ / / _ \|  __| |/ / ')
disp(' / /\  /  __/ |_| | | | (_| | | / /\  /  __/ |_ \ V  V / (_) | |  |   <  ')
disp(' \_\ \/ \___|\__,_|_|  \__,_|_| \_\ \/ \___|\__| \_/\_/ \___/|_|  |_|\_\ ')
disp('  Developed by Luca Mannella - August 2017                     (!) v0.1  ')
disp('                                                                         ')

load('..\Tic-Tac-Toe_Minimax\nn_input.txt')
load('..\Tic-Tac-Toe_Minimax\nn_output.txt')

inputs = nn_input';
targets = nn_output';

% Create a Pattern Recognition Network
hiddenLayerSize = 40;
net = patternnet(hiddenLayerSize);

% Setup Division of Data for Training, Validation, Testing
net.divideParam.trainRatio = 50/100;
net.divideParam.valRatio = 10/100;
net.divideParam.testRatio = 40/100;

% Train the Network
[net, tr] = train(net, inputs, targets);

% Test the Network
outputs = net(inputs);
errors = gsubtract(targets, outputs);
performance = perform(net, targets, outputs)

% View the Network
view(net)

% Plots
%figure, plotperform(tr)
%figure, plottrainstate(tr)
%figure, plotconfusion(targets,outputs)
%figure, ploterrhist(errors)