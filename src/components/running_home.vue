<template>
<div class="main-container">
    <div class="group">
      <div class="wrapper">
        <div class="group-2">
          <div class="box"><span class="text">9:41</span></div>
        </div>
        <div class="wrapper-2">
          <div class="box-2">
            <div class="box-3"></div>
            <div class="section"></div>
          </div>
        </div>
        <div class="box-4">
          <div class="group-3">
            <div class="pic"></div>
            <div class="pic-2"></div>
            <div class="img"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="group-4">
      <div class="group-5"><div class="img-2"></div></div>
      <span class="text-2">Details</span>
      <div class="section-2">
        <div class="group-6">
          <div class="pic-3"></div>
          <div class="img-3"></div>
          <div class="pic-4"></div>
        </div>
      </div>
    </div>
    <div class="img-4"></div>
    <div class="img-5"><div class="img-6"></div></div>
    <div class="pic-5"></div>
    <div class="img-7"></div>
    <div class="img-8"></div>
    <span class="text-3">now</span>
    <div class="pic-6"><span class="text-4">久事西郊</span></div>
    <div class="pic-7"></div>
    <div class="wrapper-3">
      <div class="box-5"></div>
      <div class="section-3">
        <div class="group-7"><div class="pic-8"></div></div>
        <div class="section-4">
          <span class="text-5">Real-time location</span
          ><span class="text-6">黑夜里两个相望的灵魂</span>
        </div>
        <div class="wrapper-4">
          <div class="img-9"></div>
          <div class="section-5">
            <span class="text-7">上</span><span class="text-8">海</span
            ><span class="text-9">，</span><span class="text-a">久事西郊</span>
          </div>
        </div>
        <div class="pic-9"></div>
        <span class="text-b">兜住你的疲惫 💤</span>
      </div>
      <div class="wrapper-5">
        <div class="wrapper-6">
          <div class="box-6">
            <div class="pic-a"></div>
            <div class="img-a"></div>
          </div>
          <div class="section-6">
            <span class="text-c">Calorie<br />consumption</span>
            <div class="wrapper-7">
              <span class="text-d">1700</span><span class="text-e">Kcal</span>
            </div>
          </div>
        </div>
        <div class="group-8">
          <div class="wrapper-8">
            <div class="img-b"></div>
            <div class="pic-b"></div>
          </div>
          <div class="wrapper-9">
            <span class="text-f">Running <br />distance</span>
            <div class="group-9">
              <span class="text-10">1.200</span><span class="text-11">m</span>
            </div>
          </div>
        </div>
      </div>
      <div class="img-c">
<div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div> 
      </div>
      <div class="box-7"></div>
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
  background: #1d1e20;
  overflow: hidden;
}
.group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  background: #1d1e20;
  backdrop-filter: blur(10px);
}
.wrapper {
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
.group-2 {
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
.box {
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
  color: #ffffff;
  font-family: SF Pro Text, var(--default-font-family);
  font-size: 16px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.32px;
  z-index: 4;
}
.wrapper-2 {
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
.box-3 {
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
.section {
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
.box-4 {
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
.pic {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.pic-2 {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.img {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.group-4 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 94px;
  position: relative;
  width: 351px;
  margin: 12px 0 0 21px;
  z-index: 46;
}
.group-5 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  padding: 19px 21px 19px 21px;
  background: #ffffff;
  z-index: 47;
  border-radius: 25.5px;
}
.img-2 {
  flex-shrink: 0;
  position: relative;
  width: 11px;
  height: 15px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/back-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 48;
}
.text-2 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 61px;
  height: 22px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 21.784px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 49;
}
.section-2 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 10px;
  position: relative;
  width: 51px;
  height: 51px;
  padding: 13px 24px 13px 24px;
  background: #ffffff;
  z-index: 50;
  border-radius: 25.5px;
}
.group-6 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 3px;
  position: relative;
  width: 3px;
  z-index: 51;
}
.pic-3 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/dot-menu-top.svg)
    no-repeat center;
  background-size: cover;
  z-index: 52;
  border-radius: 50%;
}
.img-3 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/dot-menu-middle.svg)
    no-repeat center;
  background-size: cover;
  z-index: 53;
  border-radius: 50%;
}
.pic-4 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/dot-menu-bottom.svg)
    no-repeat center;
  background-size: cover;
  z-index: 54;
  border-radius: 50%;
}
.img-4 {
  position: absolute;
  width: 273px;
  height: 273px;
  top: 135px;
  left: 57px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/main-circular-background.svg)
    no-repeat center;
  background-size: cover;
  z-index: 15;
  border-radius: 50%;
}
.img-5 {
  position: absolute;
  width: 238.129px;
  height: 123.104px;
  top: 161.372px;
  left: 83.726px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/wave-graphic.svg)
    no-repeat center;
  background-size: cover;
  z-index: 20;
}
.img-6 {
  position: relative;
  width: 22px;
  height: 22px;
  margin: 16.628px 0 0 94.274px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/small-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 59;
}
.pic-5 {
  position: absolute;
  width: 167px;
  height: 167px;
  top: 188px;
  left: 110px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/inner-circle.svg)
    no-repeat center;
  background-size: cover;
  z-index: 16;
  border-radius: 50%;
}
.img-7 {
  position: absolute;
  width: 28px;
  height: 20px;
  top: 246px;
  left: 62px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/left-control-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 22;
  overflow: hidden;
}
.img-8 {
  position: absolute;
  width: 43px;
  height: 43px;
  top: 250px;
  left: 50%;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/play-button.svg)
    no-repeat center;
  background-size: cover;
  transform: translate(-31.4%, 0);
  z-index: 17;
  overflow: hidden;
}
.text-3 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 20px;
  height: 1.29%;
  top: 31.69%;
  left: calc(50% - 128.5px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 9.147541046142578px;
  font-weight: 600;
  line-height: 11px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 19;
}
.pic-6 {
  position: absolute;
  width: 234.804px;
  height: 187.973px;
  top: 276.819px;
  left: 76.188px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/audio-waveform.svg)
    no-repeat center;
  background-size: cover;
  z-index: 21;
}
.text-4 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 32px;
  height: 5.32%;
  top: 5.95%;
  left: calc(50% - 5.59px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 8px;
  font-weight: 500;
  line-height: 9.682px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 18;
}
.pic-7 {
  position: absolute;
  width: 33px;
  height: 30.211px;
  top: 330px;
  left: 291px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/right-control-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 58;
}
.wrapper-3 {
  position: absolute;
  width: 393px;
  height: 696px;
  top: 449.819px;
  left: 0;
  background: #ffffff;
  z-index: 23;
  border-radius: 33px 33px 0 0;
}
.box-5 {
  position: relative;
  width: 99px;
  height: 2px;
  margin: 14px 0 0 147px;
  background: #d9d9d9;
  z-index: 55;
  border-radius: 1.5px;
}
.section-3 {
  position: relative;
  width: 364px;
  height: 79px;
  margin: 23.181px 0 0 16px;
  z-index: 35;
}
.group-7 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  position: absolute;
  width: 44px;
  height: 44px;
  top: 0;
  left: 320px;
  padding: 2px 7px 2px 7px;
  background: #eeeeeb;
  z-index: 25;
  overflow: hidden;
  border-radius: 43px;
}
.pic-8 {
  flex-shrink: 0;
  position: relative;
  width: 33px;
  height: 27px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/share-icon.png)
    no-repeat center;
  background-size: cover;
  z-index: 26;
}
.section-4 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 33px;
  position: absolute;
  width: 196px;
  height: 70px;
  top: 9px;
  left: 0;
  z-index: 30;
}
.text-5 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 24px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 31;
}
.text-6 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  min-width: 0;
  height: 13px;
  color: #848484;
  font-family: Inter, var(--default-font-family);
  font-size: 10.705883026123047px;
  font-weight: 500;
  line-height: 12.957px;
  text-align: left;
  white-space: nowrap;
  z-index: 32;
}
.wrapper-4 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 3px;
  position: absolute;
  width: 123px;
  height: 21px;
  top: 40px;
  left: 0;
  z-index: 27;
}
.img-9 {
  flex-shrink: 0;
  position: relative;
  width: 14px;
  height: 21px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/location-pin.svg)
    no-repeat center;
  background-size: cover;
  z-index: 28;
  overflow: hidden;
}
.section-5 {
  flex-shrink: 0;
  position: relative;
  width: 95px;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 29;
}
.text-7 {
  position: relative;
  color: #ff5218;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-transform: capitalize;
}
.text-8 {
  position: relative;
  color: #ff5218;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-transform: capitalize;
  letter-spacing: 1.26px;
}
.text-9 {
  position: relative;
  color: #ff5218;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-transform: capitalize;
  letter-spacing: -5.04px;
}
.text-a {
  position: relative;
  color: #ff5218;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-transform: capitalize;
}
.pic-9 {
  position: absolute;
  width: 87px;
  height: 23.139px;
  top: 46.861px;
  left: 277px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/rating-background.svg)
    no-repeat center;
  background-size: cover;
  z-index: 34;
}
.text-b {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: absolute;
  width: 72px;
  height: 12px;
  top: 55px;
  left: 285px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 10px;
  font-weight: 500;
  line-height: 12px;
  text-align: center;
  white-space: nowrap;
  letter-spacing: -0.2px;
  z-index: 35;
}
.wrapper-5 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 364px;
  height: 102px;
  margin: 8.819px 0 0 16px;
  z-index: 41;
}
.wrapper-6 {
  flex-shrink: 0;
  position: relative;
  width: 172px;
  height: 102px;
  background: #eeeeee;
  z-index: 36;
  border-radius: 19px;
}
.box-6 {
  position: absolute;
  width: 44px;
  height: 33px;
  top: 9.181px;
  left: 109px;
  z-index: 40;
}
.pic-a {
  position: relative;
  width: 23px;
  height: 23px;
  margin: 10px 0 0 10px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/heart-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 40;
  overflow: hidden;
}
.img-a {
  position: absolute;
  width: 44px;
  height: 44px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/profile-avatar-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 37;
  border-radius: 50%;
}
.section-6 {
  position: absolute;
  width: 94px;
  height: 73px;
  top: 19px;
  left: 19px;
  font-size: 0px;
  z-index: 39;
}
.text-c {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: relative;
  width: 85px;
  height: 34px;
  margin: 0 0 0 0;
  color: #a19d9d;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-overflow: initial;
  letter-spacing: -0.28px;
  z-index: 38;
  overflow: hidden;
}
.wrapper-7 {
  position: relative;
  width: 94px;
  height: 29px;
  margin: 10px 0 0 0;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 39;
}
.text-d {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.text-e {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.group-8 {
  flex-shrink: 0;
  position: relative;
  width: 171px;
  height: 102px;
  background: #eeeeee;
  z-index: 41;
  border-radius: 19px;
}
.wrapper-8 {
  position: absolute;
  width: 44px;
  height: 36px;
  top: 9.181px;
  left: 111px;
  z-index: 45;
}
.img-b {
  position: relative;
  width: 28px;
  height: 28px;
  margin: 8px 0 0 8px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/comment-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 45;
  overflow: hidden;
}
.pic-b {
  position: absolute;
  width: 44px;
  height: 44px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/profile-avatar-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 42;
  border-radius: 50%;
}
.wrapper-9 {
  position: absolute;
  width: 80px;
  height: 73px;
  top: 19px;
  left: 19px;
  font-size: 0px;
  z-index: 44;
}
.text-f {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: relative;
  width: 57px;
  height: 34px;
  margin: 0 0 0 0;
  color: #a19d9d;
  font-family: Inter, var(--default-font-family);
  font-size: 14px;
  font-weight: 500;
  line-height: 16.943px;
  text-align: left;
  text-overflow: initial;
  letter-spacing: -0.28px;
  z-index: 43;
  overflow: hidden;
}
.group-9 {
  position: relative;
  width: 80px;
  height: 29px;
  margin: 10px 0 0 0;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
  text-overflow: initial;
  white-space: nowrap;
  z-index: 44;
}
.text-10 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 23.638755798339844px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.text-11 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 600;
  line-height: 28.608px;
  text-align: left;
}
.img-c {
  position: relative;
  width: 364px;
  height: 87px;
  margin: 21.181px 0 0 16px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/104852/action-button-background.png)
    no-repeat center;
  background-size: cover;
  z-index: 24;
  border-radius: 29.5px;
  display: flex; 
}
.img-c > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
}
.box-7 {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 52px 0 0 130px;
  background: #000000;
  z-index: 57;
  border-radius: 100px;
}

</style>

  