<template>
<div class="main-container">
    <div class="wrapper">
      <div class="wrapper-2">
        <div class="box">
          <div class="group"><span class="text">9:41</span></div>
        </div>
        <div class="section">
          <div class="box-2">
            <div class="section-2"></div>
            <div class="wrapper-3"></div>
          </div>
        </div>
        <div class="wrapper-4">
          <div class="section-3">
            <div class="img"></div>
            <div class="img-2"></div>
            <div class="img-3"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="box-3">
      <div class="img-4"></div>
      <span class="text-2">hello,jenny!</span
      ><span class="text-3">activity overview</span>
    </div>
    <div class="box-4">
      <div class="box-5"></div>
      <div class="section-4">
        <div class="pic"></div>
        <div class="wrapper-5">
          <span class="text-4">judy-法国斗牛犬</span>
          <div class="wrapper-6">
            <span class="text-5">1 </span><span class="text-6">岁 </span
            ><span class="text-7">3</span><span class="text-8"> 个月</span>
          </div>
          <div class="pic-2"><span class="text-9">已陪伴</span></div>
        </div>
      </div>
      <div class="wrapper-7">
        <div class="pic-3"></div>
        <div class="section-5">
          <span class="text-a">judy-法国斗牛犬</span>
          <div class="wrapper-8">
            <span class="text-b">1 </span><span class="text-c">岁 </span
            ><span class="text-d">3</span><span class="text-e"> 个月</span>
          </div>
          <div class="img-5"><span class="text-f">已陪伴</span></div>
        </div>
      </div>
    </div>
    <div class="wrapper-9" @click="goToNearby">
      <div class="pic-4"></div>
      <span class="text-10">周围有趣的狗</span>
      <div class="img-6"></div>
      <div class="img-7"></div>
      <div class="img-8"></div>
      <div class="img-9"></div>
    </div>
    <div class="group-2">
      <div class="group-3">
        <div class="section-6">
          <div class="pic-5">
            <div class="group-4">
              <span class="text-11">activity overview</span
              ><span class="text-12">week</span>
              <div class="pic-6"></div>
            </div>
            <div class="pic-7">
              <div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div> 

            </div>
            <div class="wrapper-a"></div>
            <div class="box-6">
              <div class="section-7">
                <span class="text-13">卡路里：0.0</span>
              </div>
              <div class="box-7"><span class="text-14">公里：0.0</span></div>
            </div>
          </div>
        </div>
      </div>
      <div class="section-8"></div>
    </div>
  </div>
</template>
  
<script setup>
    import { useRouter } from 'vue-router';

const router = useRouter();

const goToRunning = () => {
  router.push({ name: 'running' });
};
const goToHome  = () => {
  router.push({ name: 'home' });
};
const goToNearby  = () => {
  router.push({ name: 'nearby' });
};
const goToshop  = () => {
  router.push({ name: 'shop' });
};
</script>
  
<style scoped> 
:root {
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Ubuntu, "Helvetica Neue", Helvetica, Arial, "PingFang SC",
    "Hiragino Sans GB", "Microsoft Yahei UI", "Microsoft Yahei",
    "Source Han Sans CN", sans-serif;
}

.main-container {
  overflow: hidden;
}

.main-container,
.main-container * {
  box-sizing: border-box;
}

input,
select,
textarea,
button {
  outline: 0;
}

.main-container {
  position: relative;
  width: 393px;
  height: 852px;
  margin: 0 auto;
  background: linear-gradient(180deg, #fffcdb, #ffffff);
  overflow: hidden;
}
.wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  backdrop-filter: blur(10px);
}
.wrapper-2 {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 1;
}
.box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 0 3px 10px;
  z-index: 2;
}
.group {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
  border-radius: 24px;
}
.text {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 54px;
  height: 20px;
  top: 1px;
  left: 0;
  color: #000000;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  width: 125px;
  min-height: 0;
  z-index: 5;
}
.box-2 {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.section-2 {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 7;
  overflow: hidden;
  border-radius: 100px;
}
.wrapper-3 {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 8;
  overflow: hidden;
  border-radius: 100px;
}
.wrapper-4 {
  display: flex;
  align-items: center;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-grow: 1;
  flex-shrink: 0;
  flex-basis: 0;
  gap: 8px;
  position: relative;
  min-height: 0;
  padding: 0 11px 0 0;
  z-index: 9;
}
.section-3 {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.img {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.img-2 {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.img-3 {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.box-3 {
  position: relative;
  width: 338px;
  height: 54px;
  margin: 27px 0 0 28px;
  z-index: 16;
}
.img-4 {
  position: absolute;
  width: 54px;
  height: 54px;
  top: 0;
  left: 284px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/profile-avatar.png)
    no-repeat center;
  background-size: cover;
  z-index: 16;
  border-radius: 50%;
}
.text-2 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 15px;
  top: 7px;
  left: 0;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 12.666666984558105px;
  font-weight: 600;
  line-height: 15px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 14;
}
.text-3 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 27px;
  left: 0;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 19.483333587646484px;
  font-weight: 600;
  line-height: 23.579px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 15;
}
.box-4 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 827px;
  height: 106px;
  margin: 27px 0 0 -219px;
  z-index: 20;
}
.box-5 {
  flex-shrink: 0;
  position: relative;
  width: 265px;
  height: 106px;
  background: #fff2c5;
  z-index: 20;
  border-radius: 20px;
}
.section-4 {
  flex-shrink: 0;
  position: relative;
  width: 265px;
  height: 106px;
  background: #ffe99b;
  z-index: 18;
  border-radius: 20px;
}
.pic {
  position: absolute;
  width: 76px;
  height: 81px;
  top: 12px;
  left: 10px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/114129/main-container-background.png)
    no-repeat center;
  background-size: cover;
  z-index: 22;
  border-radius: 10px;
}
.wrapper-5 {
  position: absolute;
  width: 136px;
  height: 45.375px;
  top: 28.625px;
  left: 105px;
  font-size: 0px;
  z-index: 26;
}
.text-4 {
  display: block;
  position: relative;
  height: 21px;
  margin: 0 0 0 0;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 17.399999618530273px;
  font-weight: 400;
  line-height: 21px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 23;
}
.wrapper-6 {
  position: absolute;
  width: 71px;
  height: 24px;
  top: 24.375px;
  left: 0;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 26;
}
.text-5 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.text-6 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.text-7 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.text-8 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.pic-2 {
  position: absolute;
  width: 47px;
  height: 16px;
  top: 29.375px;
  left: 80px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/rating-badge-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 24;
  border-radius: 10px;
}
.text-9 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 12px;
  top: 2px;
  left: 9px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 10px;
  font-weight: 500;
  line-height: 12px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 25;
}
.wrapper-7 {
  flex-shrink: 0;
  position: relative;
  width: 265px;
  height: 106px;
  background: #fff2c5;
  z-index: 19;
  border-radius: 20px;
}
.pic-3 {
  position: absolute;
  width: 76px;
  height: 81px;
  top: 12px;
  left: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/product-thumbnail-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 28;
  border-radius: 10px;
}
.section-5 {
  position: absolute;
  width: 136px;
  height: 45.375px;
  top: 28.625px;
  left: 108px;
  font-size: 0px;
  z-index: 32;
}
.text-a {
  display: block;
  position: relative;
  height: 21px;
  margin: 0 0 0 0;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 17.399999618530273px;
  font-weight: 400;
  line-height: 21px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 29;
}
.wrapper-8 {
  position: absolute;
  width: 71px;
  height: 24px;
  top: 24.375px;
  left: 0;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 32;
}
.text-b {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.text-c {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.text-d {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.text-e {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.img-5 {
  position: absolute;
  width: 47px;
  height: 16px;
  top: 29.375px;
  left: 80px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/rating-badge-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 30;
  border-radius: 10px;
}
.text-f {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 12px;
  top: 2px;
  left: 9px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 10px;
  font-weight: 500;
  line-height: 12px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 31;
}
.wrapper-9 {
  position: relative;
  width: 364px;
  height: 161px;
  margin: 18px 0 0 16px;
  background: #8d8d8d;
  z-index: 48;
  border-radius: 20px;
}
.pic-4 {
  position: absolute;
  width: 364px;
  height: 161px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/featured-banner.png)
    no-repeat center;
  background-size: cover;
  opacity: 0.5;
  z-index: 49;
  border-radius: 20px;
}
.text-10 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 12px;
  left: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 19.483333587646484px;
  font-weight: 600;
  line-height: 23.579px;
  text-align: left;
  white-space: nowrap;
  z-index: 50;
}
.img-6 {
  position: absolute;
  width: 38px;
  height: 43px;
  top: 16px;
  left: 291px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/feature-icon-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 52;
}
.img-7 {
  position: absolute;
  width: 76px;
  height: 76px;
  top: 45px;
  left: 143px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/feature-icon-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 51;
}
.img-8 {
  position: absolute;
  width: 38px;
  height: 43px;
  top: 81px;
  left: 44px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/feature-icon-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 54;
}
.img-9 {
  position: absolute;
  width: 38px;
  height: 43px;
  top: 107px;
  left: 247px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/feature-icon-4.png)
    no-repeat center;
  background-size: cover;
  z-index: 53;
}
.group-2 {
  position: relative;
  width: 383.475px;
  height: 542.172px;
  margin: 5.622px 0 0 5.829px;
  z-index: 35;
}
.group-3 {
  position: absolute;
  width: 380.459px;
  height: 529.753px;
  top: 0;
  left: 50%;
  background: #ffba6d;
  transform: translate(-50.02%, 0) rotate(-1.73deg);
  z-index: 35;
  border-radius: 31px;
}
.section-6 {
  position: relative;
  width: 365px;
  height: 519px;
  margin: 10.378px 0 0 7.73px;
  background: #ccedff;
  z-index: 36;
  border-radius: 31px;
}
.pic-5 {
  position: absolute;
  width: 365px;
  height: 519px;
  top: 0;
  left: 50%;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/main-product-image.png)
    no-repeat center;
  background-size: cover;
  transform: translate(-50%, 0);
  z-index: 37;
  border-radius: 31px;
}
.group-4 {
  position: relative;
  width: 304px;
  height: 39.418px;
  margin: 30px 0 0 26px;
  z-index: 41;
}
.text-11 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 167px;
  height: 39.418px;
  top: 0;
  left: 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 19.483333587646484px;
  font-weight: 600;
  line-height: 23.579px;
  text-align: left;
  text-transform: capitalize;
  z-index: 38;
}
.text-12 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 27px;
  height: 19.709px;
  top: 9.854px;
  left: 266px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 9.741666793823242px;
  font-weight: 600;
  line-height: 11.79px;
  text-align: left;
  text-transform: capitalize;
  z-index: 40;
}
.pic-6 {
  position: absolute;
  width: 7px;
  height: 4px;
  top: 15.009px;
  left: 297.5px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/dropdown-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 41;
}
.pic-7 {
  position: relative;
  width: 364px;
  height: 87px;
  margin: 198.582px 0 0 1px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113605/product-info-banner.png)
    no-repeat center;
  background-size: cover;
  z-index: 55;
  border-radius: 29.5px;
  display: flex; 

}
.pic-7 > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
}
.wrapper-a {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 16px 0 0 115px;
  background: #000000;
  z-index: 47;
  border-radius: 100px;
}
.box-6 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 334px;
  height: 68.981px;
  margin: 34px 0 0 16px;
  z-index: 44;
}
.section-7 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 162px;
  height: 68.981px;
  padding: 17px 33px 17px 33px;
  background: #000000;
  z-index: 42;
  border-radius: 43.5px;
}
.text-13 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 114px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 600;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 43;
}
.box-7 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 162px;
  height: 68.981px;
  padding: 17px 33px 17px 33px;
  background: #000000;
  z-index: 44;
  border-radius: 43.5px;
}
.text-14 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 94px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 600;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 45;
}
.section-8 {
  position: absolute;
  width: 383.475px;
  height: 528.25px;
  top: 13.921px;
  left: 50%;
  background: #ffe99b;
  transform: translate(-50%, 0) rotate(2.08deg);
  z-index: 34;
  border-radius: 31px;
}

</style>


  