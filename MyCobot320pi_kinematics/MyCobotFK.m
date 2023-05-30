clc; clear; close all;
%% Calculation of transformationmatrices for Forward Kinematics
sympref('FloatingPointOutput',true)
p = sym(pi);
o = sym('tetta', [1,6]);

T1 = ModDH(0, 0, 173.9, o(1));
T2 = ModDH(p/2, 0, 0, o(2)+p/2);
T3 = ModDH(0, 135, 0, o(3));
T4 = ModDH(0, 120, 88.78, o(4)+p/2);
T5 = ModDH(p/2, 0, 95, o(5));
T6 = ModDH(-p/2, 0, 65.5, o(6));
%Ttool = [1, 0, 0, 0;
%         0, 1, 0, 10;
%         0, 0, 1, 168;
%         0, 0, 0, 1];

T1_6 = simplify(T1*T2*T3*T4*T5*T6);

% saving important equations:
x = T1_6(1,4)
y = T1_6(2,4)
z = T1_6(3,4)

r11 = T1_6(1,1)
r21 = T1_6(2,1)
r31 = T1_6(3,1)
r32 = T1_6(3,2)
r33 = T1_6(3,3)
%% Calculation of equations/XYZRPY for Forward Kinematics
q = [143.17,-94.3,94.39,4.65,-107.05,0.35] * pi/180;
[P, O] = FK(q)