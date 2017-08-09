function [outputs, errors, performance, nRightValues, rightValuesPerc] = NeuralNetworkManual(nn_input, nn_output, hiddenLayerSize, ttPerc, plotting)

    %% Splitting inputs data in Training set and Testing Set
    j = 1; k = 1;
    for i=1:length(nn_output)
        x = rand();
        if x < ttPerc
            inputs(:,j) = nn_input(i,:)';
            targets(1,j) = nn_output(i);
            j = j+1;
        else
            tests(:,k) = nn_input(i,:)';
            test_targets(1,k) = nn_output(i);
            k = k+1;
        end
    end

    disp('Number of training samples')
    length(targets)
    disp('Number of testing samples')
    dim = length(test_targets)


    %% Create a Pattern Recognition Network with hiddenLayerSize neurons
    nRightValues = 0;
    net = patternnet(hiddenLayerSize);

    % Train the Network
    [net, tr] = train(net, inputs, targets);

    % Test the Network
    outputs = net(tests);
    errors = gsubtract(test_targets, outputs);
    performance = perform(net, test_targets, outputs);

    outputs = round(outputs);
    for i=1:dim
        if test_targets(1,i) == outputs(1,i)
            nRightValues = nRightValues + 1;
        end
    end
    rightValuesPerc = nRightValues / dim
    
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