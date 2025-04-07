<template>
<div class="main-container">
    <div class="box">
      <div class="box-2">
        <div class="box-3">
          <div class="section"><span class="text">9:41</span></div>
        </div>
        <div class="box-4">
          <div class="group">
            <div class="group-2"></div>
            <div class="box-5"></div>
          </div>
        </div>
        <div class="wrapper">
          <div class="group-3">
            <div class="img"></div>
            <div class="pic"></div>
            <div class="img-2"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="group-4">
      <span class="text-2">matches</span>
      <div class="img-3"></div>
    </div>
    <div class="box-6">
      <div class="section-2"><div class="pic-2"></div></div>
      <div class="section-3"><span class="text-3">all</span></div>
      <div class="group-5"><span class="text-4">new</span></div>
      <div class="box-7"><span class="text-5">nearby</span></div>
    </div>
    <div class="wrapper-2">
      <div class="pic-3">
        <div class="wrapper-3">
          <div class="img-4"></div>
          <span class="text-6">online</span>
        </div>
        <span class="text-7">pupu</span
        ><span class="text-8">USA.California</span>
        <div class="section-4">
          <div class="wrapper-4">
            <div class="wrapper-5"><div class="pic-4"></div></div>
          </div>
          <div class="box-8"></div>
          <div class="box-9"><div class="img-5"></div></div>
          <div class="pic-5"></div>
        </div>
      </div>
      <div class="pic-6">
        <div class="img-6">
          <div class="wrapper-6">
            <span class="text-9">she likes you!</span>
            <div class="img-7"></div>
          </div>
        </div>
      </div>
      <div class="img-8">
        <div class="group-6">
          <div class="pic-7"></div>
          <span class="text-a">online</span>
        </div>
        <span class="text-b">pupu</span
        ><span class="text-c">USA.California</span>
        <div class="box-a">
          <div class="wrapper-7">
            <div class="group-7"><div class="img-9"></div></div>
          </div>
          <div class="group-8"></div>
          <div class="group-9"><div class="img-a"></div></div>
          <div class="img-b"></div>
        </div>
      </div>
      <div class="section-5">
        <div class="box-b">
          <div class="wrapper-8">
            <div class="img-c"></div>
            <span class="text-d">Online</span>
          </div>
          <span class="text-e">pupu</span>
          <div class="box-c">
            <div class="img-d"></div>
            <div class="pic-8"></div>
            <span class="text-f">china.shanghai</span>
          </div>
        </div>
        <div class="box-d">
          <div class="pic-9"><div class="img-e"></div></div>
          <div class="pic-a"><div class="img-f"></div></div>
          <div class="img-10"><div class="img-11"></div></div>
        </div>
      </div>
    </div>
    <div class="pic-b">
<div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div> 
    </div>
    <div class="section-6"></div>
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
  background: linear-gradient(180deg, #fffcda, #ffffff);
  overflow: hidden;
}
.box {
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
.box-2 {
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
.box-3 {
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
.section {
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
.box-4 {
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
.group {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.group-2 {
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
.box-5 {
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
.wrapper {
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
.group-3 {
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
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.pic {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.img-2 {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.group-4 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 346px;
  height: 60px;
  margin: 24px 0 0 27px;
  z-index: 19;
}
.text-2 {
  flex-shrink: 0;
  position: relative;
  height: 40px;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 33.26422882080078px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 19;
}
.img-3 {
  flex-shrink: 0;
  position: relative;
  width: 60px;
  height: 60px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/profile-avatar.png)
    no-repeat center;
  background-size: cover;
  z-index: 18;
  overflow: hidden;
}
.box-6 {
  position: relative;
  width: 346px;
  height: 54px;
  margin: 5px 0 0 27px;
  z-index: 24;
}
.section-2 {
  position: absolute;
  width: 70px;
  height: 54px;
  top: 0;
  left: 0;
  background: #ffe99b;
  z-index: 20;
  border-radius: 32px;
}
.pic-2 {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 18px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/category-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 27;
  overflow: hidden;
}
.section-3 {
  position: absolute;
  width: 70px;
  height: 54px;
  top: 0;
  left: 77px;
  background: #ffe99b;
  z-index: 21;
  border-radius: 32px;
}
.text-3 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 15px;
  left: 23px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 26;
}
.group-5 {
  position: absolute;
  width: 79px;
  height: 54px;
  top: 0;
  left: 155px;
  background: #ff5218;
  z-index: 22;
  border-radius: 32px;
}
.text-4 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 15px;
  left: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 23;
}
.box-7 {
  position: absolute;
  width: 104px;
  height: 54px;
  top: 0;
  left: 242px;
  background: #ffe99b;
  z-index: 24;
  border-radius: 32px;
}
.text-5 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 24px;
  top: 15px;
  left: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 25;
}
.wrapper-2 {
  position: relative;
  width: 1041px;
  height: 465px;
  margin: 29px 0 0 -323px;
  z-index: 52;
}
.pic-3 {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/product-card-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 52;
  border-radius: 20px;
}
.wrapper-3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 56px;
  height: 17px;
  margin: 298px 0 0 23px;
  z-index: 59;
}
.img-4 {
  flex-shrink: 0;
  position: relative;
  width: 7px;
  height: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/dot-indicator.svg)
    no-repeat center;
  background-size: cover;
  z-index: 59;
  border-radius: 50%;
}
.text-6 {
  flex-shrink: 0;
  position: relative;
  height: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 54;
}
.text-7 {
  display: block;
  position: relative;
  height: 40px;
  margin: -3px 0 0 21px;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 33.26422882080078px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 53;
}
.text-8 {
  display: block;
  position: relative;
  height: 17px;
  margin: 0 0 0 23px;
  color: #707070;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 55;
}
.section-4 {
  position: relative;
  width: 296px;
  height: 53px;
  margin: 5px 0 0 21px;
  z-index: 60;
}
.wrapper-4 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 0;
  background: #ffffff;
  z-index: 56;
  border-radius: 10px;
}
.wrapper-5 {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 11px 0 0 30px;
  background: #000000;
  z-index: 63;
  overflow: visible auto;
  border-radius: 5px;
}
.pic-4 {
  position: relative;
  width: 18px;
  height: 19px;
  margin: 5px 0 0 5px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/heart-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 64;
  overflow: hidden;
}
.box-8 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 104px;
  background: #ffffff;
  opacity: 0.5;
  z-index: 57;
  border-radius: 10px;
}
.box-9 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 208px;
  background: #ff5218;
  z-index: 58;
  border-radius: 10px;
}
.img-5 {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 28px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/cart-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 61;
  overflow: hidden;
}
.pic-5 {
  position: absolute;
  width: 15.2%;
  height: 84.91%;
  top: 7.55%;
  left: 42.57%;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/plus-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 60;
  overflow: hidden;
}
.pic-6 {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 350px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/product-card-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 29;
}
.img-6 {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/product-card-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 30;
  border-radius: 20px;
}
.wrapper-6 {
  position: relative;
  width: 155px;
  height: 27px;
  margin: 16px 0 0 21px;
  background: #ff5218;
  z-index: 66;
  border-radius: 13.5px;
}
.text-9 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 19px;
  top: 5px;
  left: 32px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 67;
}
.img-7 {
  position: absolute;
  width: 9.03%;
  height: 48.15%;
  top: 29.63%;
  left: 8.39%;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/location-pin.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 68;
}
.img-8 {
  position: absolute;
  width: 339px;
  height: 447px;
  top: 0;
  left: 702px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/product-card-4.png)
    no-repeat center;
  background-size: cover;
  z-index: 38;
  border-radius: 20px;
}
.group-6 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 56px;
  height: 17px;
  margin: 298px 0 0 23px;
  z-index: 45;
}
.pic-7 {
  flex-shrink: 0;
  position: relative;
  width: 7px;
  height: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/dot-indicator-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 45;
  border-radius: 50%;
}
.text-a {
  flex-shrink: 0;
  position: relative;
  height: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 40;
}
.text-b {
  display: block;
  position: relative;
  height: 40px;
  margin: -3px 0 0 21px;
  color: #262a2b;
  font-family: Inter, var(--default-font-family);
  font-size: 33.26422882080078px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 39;
}
.text-c {
  display: block;
  position: relative;
  height: 17px;
  margin: 0 0 0 23px;
  color: #707070;
  font-family: Inter, var(--default-font-family);
  font-size: 14.137297630310059px;
  font-weight: 500;
  line-height: 17px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 41;
}
.box-a {
  position: relative;
  width: 296px;
  height: 53px;
  margin: 5px 0 0 21px;
  z-index: 46;
}
.wrapper-7 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 0;
  background: #ffffff;
  z-index: 42;
  border-radius: 10px;
}
.group-7 {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 11px 0 0 30px;
  background: #000000;
  z-index: 49;
  overflow: visible auto;
  border-radius: 5px;
}
.img-9 {
  position: relative;
  width: 18px;
  height: 19px;
  margin: 5px 0 0 5px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/heart-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 50;
  overflow: hidden;
}
.group-8 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 104px;
  background: #ffffff;
  opacity: 0.5;
  z-index: 43;
  border-radius: 10px;
}
.group-9 {
  position: absolute;
  width: 88px;
  height: 53px;
  top: 0;
  left: 208px;
  background: #ff5218;
  z-index: 44;
  border-radius: 10px;
}
.img-a {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 28px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/cart-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 47;
  overflow: hidden;
}
.img-b {
  position: absolute;
  width: 15.2%;
  height: 84.91%;
  top: 7.55%;
  left: 42.57%;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/plus-icon-2.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 46;
  overflow: hidden;
}
.section-5 {
  position: absolute;
  width: 314px;
  height: 414px;
  top: 51px;
  left: 362px;
  background: transparent;
  z-index: 100;
  border-radius: 20px;
}
.box-b {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 122px;
  margin: 227px 0 0 9px;
  z-index: 69;
}
.wrapper-8 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 5px;
  position: relative;
  width: 55px;
  z-index: 70;
}
.img-c {
  flex-shrink: 0;
  position: relative;
  width: 7px;
  height: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/dot-indicator-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 71;
}
.text-d {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 43px;
  height: 17px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 72;
}
.text-e {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 40px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 33.27004623413086px;
  font-weight: 600;
  line-height: 40px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 73;
}
.box-c {
  flex-shrink: 0;
  position: relative;
  width: 122px;
  height: 23px;
  z-index: 74;
}
.img-d {
  position: absolute;
  width: 122px;
  height: 23px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/rating-background.svg)
    no-repeat center;
  background-size: cover;
  z-index: 75;
}
.pic-8 {
  position: absolute;
  width: 18px;
  height: 17px;
  top: 3px;
  left: 7px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/star-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 76;
  overflow: hidden;
}
.text-f {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 80px;
  height: 13px;
  top: 5px;
  left: 28px;
  color: #707070;
  font-family: Inter, var(--default-font-family);
  font-size: 10.633182525634766px;
  font-weight: 500;
  line-height: 12.869px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 77;
}
.box-d {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 296px;
  height: 53px;
  margin: 12px 0 0 9px;
  z-index: 33;
}
.pic-9 {
  flex-shrink: 0;
  position: relative;
  width: 88px;
  height: 53px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/button-background-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 31;
}
.img-e {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 11px 0 0 30px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/heart-icon-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 36;
}
.pic-a {
  flex-shrink: 0;
  position: relative;
  width: 88px;
  height: 53px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/button-background-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 32;
}
.img-f {
  position: relative;
  width: 45px;
  height: 45px;
  margin: 4px 0 0 22px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/size-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 34;
  overflow: hidden;
}
.img-10 {
  flex-shrink: 0;
  position: relative;
  width: 88px;
  height: 53px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/button-background-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 33;
}
.img-11 {
  position: relative;
  width: 32px;
  height: 32px;
  margin: 11px 0 0 28px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/cart-icon-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 35;
  overflow: hidden;
}
.pic-b {
  position: relative;
  width: 364px;
  height: 87px;
  margin: 40px 0 0 16px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/105544/navigation-bar.png)
    no-repeat center;
  background-size: cover;
  z-index: 14;
  border-radius: 29.5px;
  display: flex; 

}
.pic-b > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
}
.section-6 {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 16px 0 0 130px;
  background: #000000;
  z-index: 16;
  border-radius: 100px;
}

</style>

