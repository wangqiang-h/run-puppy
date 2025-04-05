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
      <div class="flex-row">
        <div class="group"></div>
        <span class="hello-jenny">hello,jenny!</span
        ><span class="activity-overview">activity overview</span>
      </div>
      <div class="flex-row-fc">
        <div class="rectangle"></div>
        <div class="rectangle-1">
          <div class="group-2"></div>
          <div class="flex-column-ab">
            <span class="judy-french-bulldog">judy-法国斗牛犬</span>
            <div class="age-months">
              <span class="age">1 </span><span class="age-3">岁 </span
              ><span class="age-4">3</span><span class="months"> 个月</span>
            </div>
            <div class="rectangle-5"><span class="accompanied">已陪伴</span></div>
          </div>
        </div>
        <div class="rectangle-6">
          <div class="image"></div>
          <div class="flex-column-c">
            <span class="judy-french-bulldog-7">judy-法国斗牛犬</span>
            <div class="age-8">
              <span class="number-1">1 </span><span class="years">岁 </span
              ><span class="number-1-9">3</span
              ><span class="months-a"> 个月</span>
            </div>
            <div class="rectangle-b">
              <span class="already-accompanied">已陪伴</span>
            </div>
          </div>
        </div>
      </div>
      <div class="rectangle-c" @click="goToNearby">
        <div class="image-d"></div>
        <span class="people-nearby">People nearby</span>
        <div class="group-e"></div>
        <div class="group-f"></div>
        <div class="group-10"></div>
        <div class="group-11"></div>
      </div>
      <div class="flex-row-fda">
        <div class="rectangle-12">
          <div class="rectangle-13">
            <div class="group-14">
              <div class="flex-row-eb">
                <span class="activity-overview-15">activity overview</span
                ><span class="week">week</span>
                <div class="vector"></div>
              </div>
              <div class="flex-row-bc">
                <div class="frame"><span class="calories">卡路里：0.0</span></div>
                <div class="frame-16">
                  <span class="kilometers">公里：0.0</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="rectangle-17"></div>
      </div>
      <div class="frame-18">
        <div @click="goToHome"></div> 
<div @click="goToNearby"></div> 
<div @click="goToRunning"></div>
<div @click="goToshop"></div> 
      </div>

      <div class="home-indicator"></div>
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
  height: 1127px;
  margin: 0 auto;
  background: linear-gradient(180deg, #fffcdb, #ffffff);
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
  z-index: 1;
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
  z-index: 2;
}
.status-bar-time {
  flex-shrink: 0;
  position: relative;
  width: 54px;
  height: 21px;
  z-index: 3;
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
  z-index: 4;
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
  z-index: 5;
}
.status-bar-dynamic-island {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
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
  z-index: 7;
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
  z-index: 8;
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
  z-index: 9;
}
.signal-wifi-battery {
  display: flex;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 8px;
  position: relative;
  width: 78.401px;
  z-index: 10;
}
.icon-mobile-signal {
  flex-shrink: 0;
  position: relative;
  width: 18px;
  height: 12px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/mobile-signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.wifi {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/wifi-icon.svg)
    no-repeat center;
  background-size: 100% 100%;
  z-index: 12;
}
.status-bar-battery {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.flex-row {
  position: relative;
  width: 338px;
  height: 54px;
  margin: 27px 0 0 28px;
  z-index: 16;
}
.group {
  position: absolute;
  width: 54px;
  height: 54px;
  top: 0;
  left: 284px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/user-profile-photo.png)
    no-repeat center;
  background-size: cover;
  z-index: 16;
  border-radius: 50%;
}
.hello-jenny {
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
.activity-overview {
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
.flex-row-fc {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 827px;
  height: 106px;
  margin: 27px 0 0 -219px;
  z-index: 20;
}
.rectangle {
  flex-shrink: 0;
  position: relative;
  width: 265px;
  height: 106px;
  background: #fff2c5;
  z-index: 20;
  border-radius: 20px;
}
.rectangle-1 {
  flex-shrink: 0;
  position: relative;
  width: 265px;
  height: 106px;
  background: #ffe99b;
  z-index: 18;
  border-radius: 20px;
}
.group-2 {
  position: absolute;
  width: 76px;
  height: 81px;
  top: 12px;
  left: 10px;
  background: url(https://codia-f2c.s3.us-west-1.amazonaws.com/image/2025-04-05/2xsgDKgwPe.png)
    no-repeat center;
  background-size: cover;
  z-index: 22;
  border-radius: 10px;
}
.flex-column-ab {
  position: absolute;
  width: 136px;
  height: 45.375px;
  top: 28.625px;
  left: 105px;
  font-size: 0px;
  z-index: 26;
}
.judy-french-bulldog {
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
.age-months {
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
.age {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.age-3 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.age-4 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.months {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.rectangle-5 {
  position: absolute;
  width: 47px;
  height: 16px;
  top: 29.375px;
  left: 80px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/accompanied-badge.png)
    no-repeat center;
  background-size: cover;
  z-index: 24;
  border-radius: 10px;
}
.accompanied {
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
.rectangle-6 {
  flex-shrink: 0;
  position: relative;
  width: 265px;
  height: 106px;
  background: #fff2c5;
  z-index: 19;
  border-radius: 20px;
}
.image {
  position: absolute;
  width: 76px;
  height: 81px;
  top: 12px;
  left: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/second-dog-photo.png)
    no-repeat center;
  background-size: cover;
  z-index: 28;
  border-radius: 10px;
}
.flex-column-c {
  position: absolute;
  width: 136px;
  height: 45.375px;
  top: 28.625px;
  left: 108px;
  font-size: 0px;
  z-index: 32;
}
.judy-french-bulldog-7 {
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
.age-8 {
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
.number-1 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.years {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.number-1-9 {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 20px;
  font-weight: 600;
  line-height: 24px;
  text-align: left;
  text-transform: capitalize;
}
.months-a {
  position: relative;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 400;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
}
.rectangle-b {
  position: absolute;
  width: 47px;
  height: 16px;
  top: 29.375px;
  left: 80px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/already-accompanied-badge.png)
    no-repeat center;
  background-size: cover;
  z-index: 30;
  border-radius: 10px;
}
.already-accompanied {
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
.rectangle-c {
  position: relative;
  width: 364px;
  height: 161px;
  margin: 18px 0 0 16px;
  background: #8d8d8d;
  z-index: 49;
  border-radius: 20px;
}
.image-d {
  position: absolute;
  width: 364px;
  height: 161px;
  top: 0;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/people-nearby-background.png)
    no-repeat center;
  background-size: cover;
  opacity: 0.5;
  z-index: 50;
  border-radius: 20px;
}
.people-nearby {
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
  z-index: 51;
}
.group-e {
  position: absolute;
  width: 38px;
  height: 43px;
  top: 16px;
  left: 291px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/nearby-person-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 53;
}
.group-f {
  position: absolute;
  width: 76px;
  height: 76px;
  top: 45px;
  left: 143px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/nearby-person-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 52;
}
.group-10 {
  position: absolute;
  width: 38px;
  height: 43px;
  top: 81px;
  left: 44px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/nearby-person-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 55;
}
.group-11 {
  position: absolute;
  width: 38px;
  height: 43px;
  top: 107px;
  left: 247px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/nearby-person-4.png)
    no-repeat center;
  background-size: cover;
  z-index: 54;
}
.flex-row-fda {
  position: relative;
  width: 383.475px;
  height: 542.172px;
  margin: 5.622px 0 0 5.829px;
  z-index: 35;
}
.rectangle-12 {
  position: absolute;
  width: 380.459px;
  height: 529.753px;
  top: 0;
  left: 50%;
  background: #698392;
  transform: translate(-50.02%, 0) rotate(-1.73deg);
  z-index: 35;
  border-radius: 31px;
}
.rectangle-13 {
  position: relative;
  width: 365px;
  height: 519px;
  margin: 10.378px 0 0 7.73px;
  background: #ccedff;
  z-index: 36;
  border-radius: 31px;
}
.group-14 {
  position: absolute;
  width: 365px;
  height: 519px;
  top: 0;
  left: 50%;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/activity-overview-background.png)
    no-repeat center;
  background-size: cover;
  transform: translate(-50%, 0);
  z-index: 37;
  border-radius: 31px;
}
.flex-row-eb {
  position: relative;
  width: 304px;
  height: 39.418px;
  margin: 30px 0 0 26px;
  z-index: 41;
}
.activity-overview-15 {
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
.week {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  width: 27px;
  height: 19.709px;
  top: 9.854px;
  left: 266px;
  color: #74aeff;
  font-family: Inter, var(--default-font-family);
  font-size: 9.741666793823242px;
  font-weight: 600;
  line-height: 11.79px;
  text-align: left;
  text-transform: capitalize;
  z-index: 40;
}
.vector {
  position: absolute;
  width: 7px;
  height: 4px;
  top: 15.009px;
  left: 297.5px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/dropdown-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 41;
}
.flex-row-bc {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  width: 334px;
  height: 68.981px;
  margin: 340.582px 0 0 16px;
  z-index: 44;
}
.frame {
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
.calories {
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
.frame-16 {
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
.kilometers {
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
.rectangle-17 {
  position: absolute;
  width: 383.475px;
  height: 528.25px;
  top: 13.921px;
  left: 50%;
  background: #aee2ff;
  transform: translate(-50%, 0) rotate(2.08deg);
  z-index: 34;
  border-radius: 31px;
}
.frame-18 {
  position: relative;
  width: 364px;
  height: 87px;
  margin: 5.206px 0 0 16px;
  background: url(https://static.codia.ai/custom_image/2025-04-05/184336/bottom-navigation-bar.png)
    no-repeat center;
  background-size: cover;
  z-index: 46;
  border-radius: 29.5px;
  display: flex; 
}
.frame-18 > div {
            width: 25%;
            height: 100%;
            cursor: pointer;
        }
.home-indicator {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 22px 0 0 130px;
  background: #000000;
  z-index: 48;
  border-radius: 100px;
}

</style>
  