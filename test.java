class Library {

	int search(int arr[], int arr_len, int x){
	    for (int i = 0; i < arr_len; i++)
		if (arr[(int)i] == x)
		    return (int)i;
	    return -1;
	}

	int factorial(int num){
        int copyNum = num;
	    int fact = 1;
	    if(num < 0)
	    	fact = -1;
	    else{
		while(num > 1){
		    fact = fact * num--;
		}
	    }
	    return fact==verifyFactorial(copyNum)? fact:-2;
	}

	int verifyFactorial(int num){
	    int fact = 1;
	    if(num < 0){
	    	fact = -1;
	    }
	    else if(num > 1){
		    do{
			fact = fact * num;
			num = num - 1;
		     }while(num>1);
	    }
	    else {
	    	fact = 1;
	    }
	    return fact;
	}

//You can ignore following function
	public static void main(String[] args) {
// 		   int arr[] = { 1, 2, 3, 4, 5, 6 };
// 		   Library lib = new Library();
// 		   int num = 6;
// 		   int result = lib.search(arr, 6, num);
// 		   System.out.println(result);
// 		   result = lib.factorial(num);
// 		   System.out.println(result);
	}

}