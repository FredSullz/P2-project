%% Inverse Kinematics
error = [];
qArray = {};
i = 0; 

Pos_goal = [-76.77, -154.28, 514.03];
Ori_goal = [90, -30, 180]*pi/180;

%19.5738  -69.1046  -97.1254   76.2307   90.0000  199.5738

options = optimset('MaxFunEvals', 6*60000);

for n = 0:1000
    q0 = [0,0,0,0,0,0] + (rand(1,6)*2-1)*40*pi/180;
    %Solving inverse kinematics
    [q_n, error_n] = fminsearch(@(q) solve_fnc(q, Pos_goal, Ori_goal), q0, options);
    %Check results
    [Pos_n, Ori_n] = FK(q_n);
    error_n;
    q_n;
    i = i+1;
    error(i) = error_n;
    qArray{i} = q_n;
end

[M, I] = min(error);
q_min = qArray{I}
q_minDeg = q_min*180/pi
[Pos_min, Ori_min] = FK(q_min)
error(I)    
