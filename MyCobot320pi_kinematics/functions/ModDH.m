function T = ModDH(a, r, d, o)
T = [cos(o), -sin(o), 0, r;
    sin(o)*cos(a), cos(o)*cos(a), -sin(a), -sin(a)*d;
    sin(o)*sin(a), cos(o)*sin(a), cos(a), cos(a)*d;
    0, 0, 0, 1];
end