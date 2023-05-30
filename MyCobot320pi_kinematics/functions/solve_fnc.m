function error = solve_fnc(q, P_goal, O_goal)
    [P, O] = FK(q);
    O_rad = O*pi/180;
    Pos_error = P_goal - P;
    Ori_error = angdiff(O_goal, O_rad)*180/pi;

    error = sum(Pos_error.^2) + sum(Ori_error.^2);
end