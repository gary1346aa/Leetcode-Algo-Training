#include <cmath>
class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double a = 0;
        for(int i = 0; i < points.size() - 2; i++){
            for (int j = i+1; j < points.size() - 1; j++){
                for( int k = j + 1; k < points.size() ; k++){
                    double 
                        tmp = area(points[i],points[j],points[k]) ;
                    if (tmp > a)
                        a = tmp;
                }
            }
        }
        return a;
    }
    double pointDistance(vector<int> p1,vector<int> p2)  
{  
    double distance = 0;  
    distance = sqrt((p1[1]-p2[1])*(p1[1]-p2[1])+(p1[0]-p2[0])*(p1[0]-p2[0]));  
    return distance;  
}  
    double area(vector<int> p1,vector<int> p2, vector<int> p3)  
{  
    double area = 0;  
    double a = 0, b = 0, c = 0, s = 0;  
    a = pointDistance(p1, p2);  
    b = pointDistance(p2, p3);  
    c = pointDistance(p1, p3);  
    s = 0.5*(a+b+c);  
    area = sqrt(s*(s-a)*(s-b)*(s-c));  
    return area;  
}  

};