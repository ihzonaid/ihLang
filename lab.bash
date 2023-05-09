echo Welcome to Bash loop

# for num in 1 2 3 4 5
# do
#     echo $num
# done

read -p "Enter number: " x 

count=1
sum=0

factorial=1
while [ $count -lt $x ]
do
    sum=$(($sum+count))
    count=$(($count+1))
    factorial=$(($factorial*$count))
done

# echo summation: $sum
echo factoria: $factorial


