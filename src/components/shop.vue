<template>
<div class="main-container">
    <div class="top-navigation">
      <div class="status-bar">
        <div class="left-side">
          <div class="status-bar-time"><span class="time">9:41</span></div>
        </div>
        <div class="dynamic-island">
          <div class="status-bar-dynamic-island">
            <div class="true-depth-camera"></div>
            <div class="facetime-camera"></div>
          </div>
        </div>
        <div class="right-side">
          <div class="signal-wifi-battery">
            <div class="icon-mobile-signal"></div>
            <div class="wifi"></div>
            <div class="status-bar-battery"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="frame">
      <div class="magnifier"></div>
      <span class="text-2">Search here</span>
    </div>
    <span class="text-3">Results of the week</span>
    <div class="group-5">
      <div class="section-4">
        <span class="text-4">mon</span><span class="text-5">tue</span
        ><span class="text-6">wed</span><span class="text-7">thu</span
        ><span class="text-8">fri</span><span class="text-9">sat</span
        ><span class="text-a">sun</span>
      </div>
      <div class="section-5">
        <div class="pic-3"></div>
        <div class="img-3"></div>
        <div class="img-4"></div>
        <div class="pic-4"></div>
        <div class="pic-5"></div>
        <div class="img-5"></div>
        <div class="img-6"></div>
      </div>
    </div>
    <div class="img-7" @click="goVIP">
      <div class="section-6">
        <span class="text-b">成为<br />俱乐部vip</span>
      </div>
      <div class="group-6"><span class="text-c">加入会员</span></div>
    </div>
    <div class="pic-6"></div>
    <div class="img-8"></div>
    <span class="text-d">Run<br />Puppy</span>
    <div class="wrapper-3">
      <span class="text-e">Recommendation</span>
      <div class="section-7">
        <div class="group-7">
          <div class="group-8">
            <div class="img-9"></div>
            <div class="section-8">
              <span class="text-f">圣诞节限定衣服</span
              ><span class="text-10">$123,00</span>
            </div>
            <div class="wrapper-4">
              <div class="img-a"></div>
              <span class="text-11">4.7</span>
            </div>
          </div>
          <div class="group-9">
            <div class="pic-7"></div>
            <div class="section-9">
              <span class="text-12">小狗眼镜</span
              ><span class="text-13">$123,00</span>
            </div>
            <div class="section-a">
              <div class="img-b"></div>
              <span class="text-14">4.7</span>
            </div>
          </div>
        </div>
        <div class="group-a">
          <div class="box-3">
            <div class="pic-8"></div>
            <div class="group-b">
              <span class="text-15">Siamese Cat</span
              ><span class="text-16">$123,00</span>
            </div>
            <div class="box-4">
              <div class="pic-9"></div>
              <span class="text-17">4.7</span>
            </div>
          </div>
          <div class="box-5">
            <div class="img-c"></div>
            <div class="section-b">
              <span class="text-18">Siamese Cat</span
              ><span class="text-19">$123,00</span>
            </div>
            <div class="box-6">
              <div class="pic-a"></div>
              <span class="text-1a">4.7</span>
            </div>
          </div>
        </div>
      </div>
      <span class="text-1b">See All</span>
    </div>
    <div class="img-d">
<div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div>  
    </div>
    <div class="wrapper-5"></div>
  </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goVIP = () => {
  router.push({ name: 'vip' });
};
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
  background: linear-gradient(180deg, #fffcdd, #ffffff);
  overflow: hidden;
}
.top-navigation {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 2px;
  position: relative;
  width: 393px;
  margin: 0 0 0 0;
  z-index: 70;
  backdrop-filter: blur(10px);
}
.status-bar {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 59px;
  z-index: 71;
}
.left-side {
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
  z-index: 72;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 73;
  border-radius: 24px;
}
.time {
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
  z-index: 74;
}
.dynamic-island {
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
  z-index: 75;
}
.status-bar-dynamic-island {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 76;
  border-radius: 100px;
}
.true-depth-camera {
  position: absolute;
  width: 80px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(-78.13%, -50%);
  z-index: 77;
  overflow: hidden;
  border-radius: 100px;
}
.facetime-camera {
  position: absolute;
  width: 37px;
  height: 37px;
  top: 50%;
  left: 50%;
  background: #000000;
  transform: translate(68.92%, -50%);
  z-index: 78;
  overflow: hidden;
  border-radius: 100px;
}
.right-side {
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
  z-index: 79;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 80;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 81;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 82;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 83;
}
.frame {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10.342px;
  position: relative;
  width: 355.761px;
  height: 55.846px;
  margin: 73.427px 0 0 20px;
  padding: 14.479px 17.581px 14.479px 17.581px;
  background: #f2f5f7;
  z-index: 2;
  overflow: hidden;
  border-radius: 27.923px;
}
.magnifier {
  flex-shrink: 0;
  position: relative;
  width: 26.889px;
  height: 26.889px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/magnifier-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 3;
  overflow: hidden;
}
.text-2 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 95px;
  height: 20px;
  color: #d4d4d4;
  font-family: Inter, var(--default-font-family);
  font-size: 16.547008514404297px;
  font-weight: 500;
  line-height: 20px;
  text-align: center;
  white-space: nowrap;
  z-index: 4;
}
.text-3 {
  display: block;
  position: relative;
  height: 22px;
  margin: 15.513px 0 0 20px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18.00165367126465px;
  font-weight: 600;
  line-height: 21.786px;
  text-align: left;
  white-space: nowrap;
  z-index: 28;
}
.group-5 {
  position: relative;
  width: 355.761px;
  height: 65.154px;
  margin: 7.992px 0 0 20px;
  background: #ffe99b;
  z-index: 7;
  overflow: visible auto;
  border-radius: 14px;
}
.section-4 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 249.59px;
  height: 11px;
  margin: 17.581px 0 0 53.778px;
  z-index: 14;
}
.text-4 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 22px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 8;
}
.text-5 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 19px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 9;
}
.text-6 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 22px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 10;
}
.text-7 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 20px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 11;
}
.text-8 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 14px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 12;
}
.text-9 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 13;
}
.text-a {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  position: relative;
  width: 20px;
  height: 11px;
  color: #5f5f5f;
  font-family: Inter, var(--default-font-family);
  font-size: 9.040648460388184px;
  font-weight: 600;
  line-height: 10.941px;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  z-index: 14;
}
.section-5 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 243.034px;
  height: 15.513px;
  margin: 4.513px 0 0 57.915px;
  z-index: 21;
}
.pic-3 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/profile-pic-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 15;
  border-radius: 50%;
}
.img-3 {
  flex-shrink: 0;
  position: relative;
  width: 14.479px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/category-icon-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 16;
}
.img-4 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/profile-pic-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 17;
  border-radius: 50%;
}
.pic-4 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/profile-pic-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 18;
  border-radius: 50%;
}
.pic-5 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/profile-pic-4.svg)
    no-repeat center;
  background-size: cover;
  z-index: 19;
  border-radius: 50%;
}
.img-5 {
  flex-shrink: 0;
  position: relative;
  width: 14.479px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/category-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 20;
}
.img-6 {
  flex-shrink: 0;
  position: relative;
  width: 15.513px;
  height: 15.513px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/profile-pic-5.svg)
    no-repeat center;
  background-size: cover;
  z-index: 21;
  border-radius: 50%;
}
.img-7 {
  position: relative;
  width: 355.761px;
  height: 85.838px;
  margin: 8.273px 0 0 20px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/banner-image.png)
    no-repeat center;
  background-size: cover;
  z-index: 23;
  border-radius: 14px;
}
.section-6 {
  position: absolute;
  width: 100.316px;
  height: 58.949px;
  top: 13.444px;
  left: 97.214px;
  background: #fcfdff;
  z-index: 24;
  border-radius: 13.444px;
}
.text-b {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 87px;
  height: 38px;
  top: 10.342px;
  left: 10.342px;
  color: #111b27;
  font-family: JingNanYuanMoT, var(--default-font-family);
  font-size: 18.735557556152344px;
  font-weight: 900;
  line-height: 19.335px;
  text-align: left;
  text-transform: capitalize;
  z-index: 25;
}
.group-6 {
  position: absolute;
  width: 69.291px;
  height: 31.026px;
  top: 27.923px;
  left: 267.855px;
  background: #ff5218;
  z-index: 26;
  border-radius: 8.274px;
}
.text-c {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 15px;
  top: 8.273px;
  left: 9.308px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 12.774243354797363px;
  font-weight: 900;
  line-height: 15px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 27;
}
.pic-6 {
  position: absolute;
  width: 62.051px;
  height: 62.051px;
  top: 59px;
  left: 320.949px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/circular-profile.svg)
    no-repeat center;
  background-size: cover;
  overflow: hidden;
}
.img-8 {
  position: absolute;
  width: 36.197px;
  height: 40.334px;
  top: 70.376px;
  left: 22.068px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/logo-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 68;
  overflow: hidden;
}
.text-d {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 54px;
  height: 32px;
  top: 73.479px;
  left: 65.538px;
  color: #000000;
  font-family: Tsukushi B Round Gothic, var(--default-font-family);
  font-size: 15.862500190734863px;
  font-weight: 400;
  line-height: 15.863px;
  text-align: left;
  text-overflow: initial;
  text-transform: uppercase;
  z-index: 69;
  overflow: hidden;
  -webkit-text-stroke: 1.367px #000000;
}
.wrapper-3 {
  display: flex;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 10px;
  position: absolute;
  width: 355.761px;
  height: 550.188px;
  top: 415.795px;
  left: 20px;
  z-index: 29;
}
.text-e {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-basis: auto;
  position: relative;
  width: 153px;
  height: 22px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 18.00165367126465px;
  font-weight: 600;
  line-height: 21.786px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 30;
}
.section-7 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  gap: 17.581px;
  position: relative;
  width: 355.761px;
  z-index: 32;
}
.group-7 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  z-index: 33;
}
.group-8 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 34;
}
.img-9 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/product-image-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 35;
  border-radius: 22.752px;
}
.section-8 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 36;
}
.text-f {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 500;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 37;
}
.text-10 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 38;
}
.wrapper-4 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 39;
  overflow: hidden;
  border-radius: 12.927px;
}
.img-a {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/rating-icon-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 40;
  border-radius: 0.52px;
}
.text-11 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 41;
}
.group-9 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 42;
}
.pic-7 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/product-image-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 43;
  border-radius: 22.752px;
}
.section-9 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 44;
}
.text-12 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 500;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 45;
}
.text-13 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 46;
}
.section-a {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 47;
  overflow: hidden;
  border-radius: 12.927px;
}
.img-b {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/rating-icon-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 48;
  border-radius: 0.52px;
}
.text-14 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 49;
}
.group-a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  z-index: 50;
}
.box-3 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 51;
}
.pic-8 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/product-image-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 52;
  border-radius: 22.752px;
}
.group-b {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 53;
}
.text-15 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 54;
}
.text-16 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 55;
}
.box-4 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 56;
  overflow: hidden;
  border-radius: 12.927px;
}
.pic-9 {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/rating-icon-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 57;
  border-radius: 0.52px;
}
.text-17 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 58;
}
.box-5 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8.274px;
  position: relative;
  width: 173.744px;
  z-index: 59;
}
.img-c {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 186.154px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/product-image-4.png)
    no-repeat center;
  background-size: cover;
  z-index: 60;
  border-radius: 22.752px;
}
.section-b {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-self: stretch;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 4.137px;
  position: relative;
  min-width: 0;
  height: 51.709px;
  padding: 7.239px 0 7.239px 0;
  z-index: 61;
}
.text-18 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 62;
}
.text-19 {
  align-self: stretch;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 19px;
  color: #f96a36;
  font-family: Inter, var(--default-font-family);
  font-size: 16.031185150146484px;
  font-weight: 600;
  line-height: 19px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 63;
}
.box-6 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  flex-shrink: 0;
  position: absolute;
  width: 55.846px;
  height: 25.855px;
  top: 10.342px;
  left: 105.487px;
  padding: 2.068px 7.239px 2.068px 7.239px;
  background: #ffffff;
  z-index: 64;
  overflow: hidden;
  border-radius: 12.927px;
}
.pic-a {
  flex-shrink: 0;
  position: relative;
  width: 17.582px;
  height: 17.582px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/rating-icon-4.svg)
    no-repeat center;
  background-size: cover;
  z-index: 65;
  border-radius: 0.52px;
}
.text-1a {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 16px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 13.499946594238281px;
  font-weight: 500;
  line-height: 16px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 66;
}
.text-1b {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-basis: auto;
  position: relative;
  width: 44px;
  height: 16px;
  color: #b7b7b7;
  font-family: Inter, var(--default-font-family);
  font-size: 13.346052169799805px;
  font-weight: 500;
  line-height: 16px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 100;
}
.img-d {
  position: absolute;
  width: 364px;
  height: 87px;
  top: 736px;
  left: 16px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/112032/navigation-bar.png)
    no-repeat center;
  background-size: cover;
  z-index: 86;
  border-radius: 29.5px;
  display: flex; 

}
.img-d > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
}
.wrapper-5 {
  position: absolute;
  height: 5px;
  right: 129px;
  bottom: 8px;
  left: 130px;
  background: #000000;
  z-index: 85;
  border-radius: 100px;
}

</style>

  