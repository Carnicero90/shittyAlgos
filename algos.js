function rota(l1, l2) {
	if (l1.length == l2.length) {
		const k = l1[0];
		for (let i = 0; i < l1.length; i++) {
			if ((l2[i] == k) && (l1.join() == l2.slice(i) + ',' + l2.slice(0, i))) {
				return true
			}
		}
	}
	return False
}

console.log(rota([1, 2, 3], [2, 3, 1]))
