function [] = NN_Train_Test(len, inputs, targets, trainingPerc, validatingPerc, testingPerc)

    %% 10 hidden neurons
    [outputs10, errors10, performance10, nRightValues10] = NeuralNetwork(inputs, targets, 10, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 10 neurons in the hidden layer')
    nRightValues10
    perc = nRightValues10 / len
    performance10


    %% 50 hidden neurons
    [outputs50, errors50, performance50, nRightValues50] = NeuralNetwork(inputs, targets, 50, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 50 neurons in the hidden layer')
    nRightValues50
    perc = nRightValues50 / len
    performance50


    %% 100 hidden neurons
    [outputs100, errors100, performance100, nRightValues100] = NeuralNetwork(inputs, targets, 100, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 100 neurons in the hidden layer')
    nRightValues100
    perc = nRightValues100 / len
    performance100


    %% 120 hidden neurons
    [outputs120, errors120, performance120, nRightValues120] = NeuralNetwork(inputs, targets, 120, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 120 neurons in the hidden layer')
    nRightValues120
    perc = nRightValues120 / len
    performance120


    %% 250 hidden neurons
    %[outputs250, errors250, performance250, nRightValues250] = NeuralNetwork(inputs, targets, 250, trainingPerc, validatingPerc, testingPerc, false);

    %disp('Number of correct values using 250 neurons in the hidden layer')
    %nRightValues250
    %perc = nRightValues250 / len
    %performance250


    %% 500 hidden neurons
    [outputs500, errors500, performance500, nRightValues500] = NeuralNetwork(inputs, targets, 500, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 500 neurons in the hidden layer')
    nRightValues500
    perc = nRightValues500 / len
    performance500


    %% 750 hidden neurons
    %[outputs750, errors750, performance750, nRightValues750] = NeuralNetwork(inputs, targets, 750, trainingPerc, validatingPerc, testingPerc, false);

    %disp('Number of correct values using 750 neurons in the hidden layer')
    %nRightValues750
    %perc = nRightValues750 / len
    %performance750


    %% 1000 hidden neurons
    [outputs1000, errors1000, performance1000, nRightValues1000] = NeuralNetwork(inputs, targets, 1000, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 1000 neurons in the hidden layer')
    nRightValues1000
    perc = nRightValues1000 / len
    performance1000


    %% 1100 hidden neurons
    [outputs1100, errors1100, performance1100, nRightValues1100] = NeuralNetwork(inputs, targets, 1100, trainingPerc, validatingPerc, testingPerc, false);

    disp('Number of correct values using 1100 neurons in the hidden layer')
    nRightValues1100
    perc = nRightValues1100 / len
    performance1100

end