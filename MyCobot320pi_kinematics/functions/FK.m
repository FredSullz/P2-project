function [P, O] = FK(q)
o1 = q(1); o2 = q(2); o3 = q(3);
o4 = q(4); o5 = q(5); o6 = q(6);

X = 88.7800*sin(o1) - 135*cos(o1)*sin(o2) + 65.5000*cos(o5)*sin(o1) - 120*cos(o1)*cos(o2)*sin(o3) - 120*cos(o1)*cos(o3)*sin(o2) - 95*cos(o1)*cos(o2)*cos(o3)*sin(o4) - 95*cos(o1)*cos(o2)*cos(o4)*sin(o3) - 95*cos(o1)*cos(o3)*cos(o4)*sin(o2) + 95*cos(o1)*sin(o2)*sin(o3)*sin(o4) + 65.5000*cos(o1)*cos(o2)*cos(o3)*cos(o4)*sin(o5) - 65.5000*cos(o1)*cos(o2)*sin(o3)*sin(o4)*sin(o5) - 65.5000*cos(o1)*cos(o3)*sin(o2)*sin(o4)*sin(o5) - 65.5000*cos(o1)*cos(o4)*sin(o2)*sin(o3)*sin(o5);
Y = 95*sin(o1)*sin(o2)*sin(o3)*sin(o4) - 65.5000*cos(o1)*cos(o5) - 135*sin(o1)*sin(o2) - 120*cos(o2)*sin(o1)*sin(o3) - 120*cos(o3)*sin(o1)*sin(o2) - 95*cos(o2)*cos(o3)*sin(o1)*sin(o4) - 95*cos(o2)*cos(o4)*sin(o1)*sin(o3) - 95*cos(o3)*cos(o4)*sin(o1)*sin(o2) - 88.7800*cos(o1) + 65.5000*cos(o2)*cos(o3)*cos(o4)*sin(o1)*sin(o5) - 65.5000*cos(o2)*sin(o1)*sin(o3)*sin(o4)*sin(o5) - 65.5000*cos(o3)*sin(o1)*sin(o2)*sin(o4)*sin(o5) - 65.5000*cos(o4)*sin(o1)*sin(o2)*sin(o3)*sin(o5);
Z = 95*cos(o2 + o3 + o4) - 32.7500*cos(o2 + o3 + o4 + o5) + 120*cos(o2 + o3) + 135*cos(o2) + 32.7500*cos(o2 + o3 + o4 - o5) + 173.9000;


R11 = cos(o6)*(sin(o1)*sin(o5) - cos(o1)*cos(o2)*cos(o3)*cos(o4)*cos(o5) + cos(o1)*cos(o2)*cos(o5)*sin(o3)*sin(o4) + cos(o1)*cos(o3)*cos(o5)*sin(o2)*sin(o4) + cos(o1)*cos(o4)*cos(o5)*sin(o2)*sin(o3)) + sin(o2 + o3 + o4)*cos(o1)*sin(o6);
R21 = cos(o6)*(cos(o2)*cos(o5)*sin(o1)*sin(o3)*sin(o4) - cos(o2)*cos(o3)*cos(o4)*cos(o5)*sin(o1) - cos(o1)*sin(o5) + cos(o3)*cos(o5)*sin(o1)*sin(o2)*sin(o4) + cos(o4)*cos(o5)*sin(o1)*sin(o2)*sin(o3)) + sin(o2 + o3 + o4)*sin(o1)*sin(o6);
R31 = 0.5000*sin(o2 + o3 + o4 - o6) - 0.5000*sin(o2 + o3 + o4 + o6) - sin(o2 + o3 + o4)*cos(o5)*cos(o6);

R32 = sin(o2 + o3 + o4)*cos(o5)*sin(o6) - 0.5000*cos(o2 + o3 + o4 - o6) - 0.5000*cos(o2 + o3 + o4 + o6);
R33 = 0.5000*cos(o2 + o3 + o4 - o5) - 0.5000*cos(o2 + o3 + o4 + o5);

theta_x = atan2(-R32, R33);
theta_y = atan2(R31, (R11^2+R21^2)^0.5);
theta_z = atan2(-R21, R11);

theta_x_deg = theta_x * 180/pi;
theta_y_deg = theta_y * 180/pi;
theta_z_deg = theta_z * 180/pi;

P = [X,Y,Z];
O = [theta_x_deg, theta_y_deg, theta_z_deg];
end