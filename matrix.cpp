#include "../Horde3D/Horde3D/Source/Shared/utMath.h"
#include "matrix.h"
#include <stdio.h>
extern "C" {
	void *matrixFromFloats(const float* floats){
		return new Horde3D::Matrix4f(floats);
	}
	void *newUnitMatrix(){
		return new Horde3D::Matrix4f();
	}
	void rotateMatrix(void* matrix, float x, float y, float z ){
		Horde3D::Matrix4f* m = (Horde3D::Matrix4f*) matrix;
		(*m).rotate(x*3.141592646/360,y*3.141592646/360,z*3.141592646/360);
	}
	void translateMatrix(void *matrix, const float x, const float y, const float z ){
		Horde3D::Matrix4f* m = (Horde3D::Matrix4f*) matrix;
		(*m).translate(x,y,z);
	}
	void scaleMatrix(void *matrix, const float x, const float y, const float z ){
		((Horde3D::Matrix4f*) matrix)->scale(x,y,z);
	}
	float* floatsFromMatrix(void *matrix){
		return (float*) &((Horde3D::Matrix4f*) matrix)->x;
	}
	void updateMatrixFromFloats(void *matrix, const float* floats){
		int i;
		float f;
		
		for (i=0;i<16;i++){
			f = (float) *(floats+i);
			((Horde3D::Matrix4f*) matrix)->x[i]=f;
		}
	}
	void rotationFromMatrix(void *matrix, float* rotation){
		Horde3D::Matrix4f *m = ((Horde3D::Matrix4f*) matrix);
		Horde3D::Vec3f trans;
		Horde3D::Vec3f rot;
		Horde3D::Vec3f scale;
		m->decompose(trans, rot, scale);
		rotation[0]=rot.x*180 / 3.14159265;
		rotation[1]=rot.y*180 / 3.14159265;
		rotation[2]=rot.z*180 / 3.14159265;
	}
	void scaleFromMatrix(void *matrix, float *Scale){
		Horde3D::Matrix4f *m = ((Horde3D::Matrix4f*) matrix);
		Horde3D::Vec3f trans;
		Horde3D::Vec3f rot;
		Horde3D::Vec3f scale;
		m->decompose(trans, rot, scale);
		Scale[0]=scale.x;
		Scale[1]=scale.y;
		Scale[2]=scale.z;
	}
	void translationFromMatrix(void *matrix, float* Trans){
		Horde3D::Matrix4f *m = ((Horde3D::Matrix4f*) matrix);
		Horde3D::Vec3f trans;
		Horde3D::Vec3f rot;
		Horde3D::Vec3f scale;
		m->decompose(trans, rot, scale);
		Trans[0]=trans.x;
		Trans[1]=trans.y;
		Trans[2]=trans.z;
	}
}

void tst(void *matrix){
	Horde3D::Matrix4f *m = ((Horde3D::Matrix4f*) matrix);
	float d[16];
	rotationFromMatrix(m, d);
	printf("Roll: %f, Pitch: %f, Yaw: %f\n", *d,*(d+1),*(d+2));
}

void tst1(void *matrix){
	Horde3D::Matrix4f m = *((Horde3D::Matrix4f*) matrix);
	tst(matrix);
	rotateMatrix((Horde3D::Matrix4f*) matrix, 1,0,0);
	tst(&m);
}

int main(){
	float f[16];
	float d[16];
	Horde3D::Matrix4f m;
	Horde3D::Matrix4f *M;
	M = new Horde3D::Matrix4f();
	m = *M;
	float* t = &M->x[0];
	
	translationFromMatrix(M,f);
	printf("Test <%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f>\n",*t,*(t+1),*(t+2),*(t+3),*(t+4),*(t+5),*(t+6),*(t+7),*(t+8),*(t+9),*(t+10),*(t+11),*(t+12),*(t+13),*(t+14),*(t+15));
	printf("%fi+%fj+%fk\n",*f,*(f+1),*(f+2));
	M->translate(10,11,12);
	translationFromMatrix(M,f);
	printf("%fi+%fj+%fk\n",*f,*(f+1),*(f+2));
	printf("Test <%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f>\n",*t,*(t+1),*(t+2),*(t+3),*(t+4),*(t+5),*(t+6),*(t+7),*(t+8),*(t+9),*(t+10),*(t+11),*(t+12),*(t+13),*(t+14),*(t+15));
	
	
	//printf("Roll: %f, Pitch: %f, Yaw: %f\n", *d,*(d+1),*(d+2));
	
	
	return 0;
}

