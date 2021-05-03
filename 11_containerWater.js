// Given n non-negative integers a1, a2, ..., an , where each represents a point
// at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
// the line i is at (i, ai) and (i, 0). Find two lines, which, together with
// the x-axis forms a container, such that the container contains the most water.

// Input: height = [4,3,2,1,4]
// Output: 16

// Input: height = [1,1]
// Output: 1

// INPUT = [1,8,6,2,5,4,8,3,7]
// Output = 49

const solution1 = (height) => {
  let max = 0;
  let area = 0;
  for (i = 0; i < height.length; i++) {
    for (j = i + 1; j <= height.length; j++) {
      if (height[j] > height[i]) {
        area = height[i] * (j - i);
      } else {
        area = height[j] * (j - i);
      }
      if (area > max) {
        max = area;
      }
    }
  }
  return max;
};

const solution2 = (height) => {
  let areaMax = 0;
  let area = 0;
  let head = 0;
  let tail = height.length - 1;
  console.log(Math.ceil(height.length / 2));

  for (c = 0; c <= height.length; c++) {
    if (height[head] < height[tail]) {
      area = height[head] * (tail - head);
      head++;
    } else {
      area = height[tail] * (tail - head);
      tail--;
    }
    if (area > areaMax) {
      areaMax = area;
    }
  }
  return areaMax;

};

// height = [4, 3, 2, 1, 4];
// height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
// height = [1, 1];
height = [2,3,4,5,18,17,6]
console.log(solution1(height));
console.log(solution2(height));
