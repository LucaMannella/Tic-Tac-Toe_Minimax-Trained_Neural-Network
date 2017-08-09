function [outputs, errors, performance, nRightValues] = NeuralNetwork(inputs, targets, hiddenLayerSize, trainingPerc, validationPerc, testingPerc, plotting)

    %% Create a Pattern Recognition Network with hiddenLayerSize neurons
    nRightValues = 0;
    net = patternnet(hiddenLayerSize);

    % Setup Division of Data for Training, Validation, Testing
    net.divideParam.trainRatio = trainingPerc;
    net.divideParam.valRatio = validationPerc;
    net.divideParam.testRatio = testingPerc;

    % Train the Network
    [net, tr] = train(net, inputs, targets);

    % Test the Network
    outputs = net(inputs);
    errors = gsubtract(targets, outputs);
    performance = perform(net, targets, outputs);

    outputs = round(outputs);
    for i=1:length(targets)
        if targets(1,i) == outputs(1,i)
            nRightValues = nRightValues + 1;
        end
    end
    
    if plotting
        % View the Network
        view(net)

        % Plots
        figure, plotperform(tr)
        figure, plottrainstate(tr)
        figure, plotconfusion(targets, outputs)
        figure, ploterrhist(errors)
    end
end