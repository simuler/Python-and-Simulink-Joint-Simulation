% ------------------------------------------------------------------
% FileName:         CoC2C4_step.m
% Author:           宁文彬
% Github:           http://github.com/simuler
% Version:          V 1.0
% Description:      草酸钴合成过程gym环境step函数
% ------------------------------------------------------------------

function [out] = CoC2O4_step(action, time)

    pause(1); % pause很关键，后续讨论
    set_param('CoC2O4withoutT7/pause_time','value',num2str(time));% 修改下一个pause_time
    set_param('CoC2O4withoutT7/Fb','value',num2str(action));% 修改控制变量u
    set_param('CoC2O4withoutT7', 'SimulationCommand', 'continue'); % continue

    C = evalin('caller', 'C.signals.values(end)');
    V = evalin('caller', 'V.signals.values(end)');
    mu0 = evalin('caller', 'mu0.signals.values(end)');
    mu1 = evalin('caller', 'mu1.signals.values(end)');
    mu2 = evalin('caller', 'mu2.signals.values(end)');
    mu3 = evalin('caller', 'mu3.signals.values(end)');

    out = [C, V, mu0, mu1, mu2, mu3];
    if time == 660
        set_param('CoC2O4withoutT7', 'SimulationCommand', 'stop'); % stop
    end
end