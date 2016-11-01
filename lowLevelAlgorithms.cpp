int numberOfOnes (int32_t a) {
	int count = 0;

	while (a != 0) {
		count += 1;
		a = a - (a & ~(a - 1));
	}

	return count;
}