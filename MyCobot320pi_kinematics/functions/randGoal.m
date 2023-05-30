function [Pos_goal, Ori_goal, q_find] = randGoal()
    q_find = rand(1,6)*2*pi-pi
    [Pos_goal, Ori_goal] = FK(q_find)
end
