#ifdef __cplusplus
extern "C" {
#endif
	void *matrixFromFloats(const float* floats);
	void *newUnitMatrix();
	void rotateMatrix(void *matrix, const float x, const float y, const float z );
	void translateMatrix(void *matrix, const float x, const float y, const float z );
	void scaleMatrix(void *matrix, const float x, const float y, const float z );
	float* floatsFromMatrix(void *matrix);
	void translationFromMatrix(void *matrix, float* Trans);
	void rotationFromMatrix(void *matrix, float* Rotation);
	void scaleFromMatrix(void *matrix, float* Scale);
	void updateMatrixFromFloats(void *matrix, const float* floats);
	void tst(void *matrix);
	void tst1(void *matrix);
#ifdef __cplusplus
}
#endif
