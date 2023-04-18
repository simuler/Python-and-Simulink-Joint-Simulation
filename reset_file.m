% ------------------------------------------------------------------
% FileName:         reset_file.m
% Author:           宁文彬
% Github:           http://github.com/simuler
% Version:          V 1.0
% Description:      草酸钴合成过程gym环境重置环境
% ------------------------------------------------------------------

clear all;
clear clc;

set_param('CoC2O4withoutT7','StopTime','720');  % 设定仿真截止时间
% Simulink.suppressDiagnostic('CoC2O4withoutT7/Assertion', 'Simulink:blocks:AssertionAssert');
set_param('CoC2O4withoutT7', 'SimulationCommand', 'start'); % 开启控制，会在0s自动pause
set_param('CoC2O4withoutT7', 'SimulationCommand', 'pause'); % 开启控制，会在0s自动pauses