Given a sequence A<sub>1</sub>, A<sub>2</sub>,..., A<sub>N</sub>.

Find the max. possible difference between the sum of all elements of subsequence S of length K such that S<sub>1</sub> >= S<sub>2</sub> >= ... >= S<sub>k</sub>
and the sum of all elements of subsequence D of length same as S such that D<sub>1</sub> <= D<sub>2</sub> <= ... <= D<sub>k</sub>.

i.e. (S<sub>1</sub> + S<sub>2</sub> + S<sub>3</sub> + ... + S<sub>k</sub>) - (D<sub>1</sub> + D<sub>2</sub> + D<sub>3</sub> + ... + D<sub>k</sub>)

Elements of both subsequences ,ay be same or different

Return -1 if subsequence does not exist
