import add_work
import mul_work
import sub_work
import div_work

a = 100
b = 50 

total_sum = add_work.add(a,b)
total_sub = sub_work.sub(a,b)
total_mul = mul_work.mul(a,b)
div_work = div_work.div(a,b)

print(f"Total sum is {total_sum}. Total sub is {total_sub}. Total mul is {total_mul}. Total div is {div_work}")