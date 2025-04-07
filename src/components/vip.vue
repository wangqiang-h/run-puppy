<template>
  <div class="main-container">
    <div class="wrapper">
      <div class="group">
        <div class="section">
          <div class="group-2"><span class="text">9:41</span></div>
        </div>
        <div class="group-3">
          <div class="section-2">
            <div class="wrapper-2"></div>
            <div class="section-3"></div>
          </div>
        </div>
        <div class="section-4">
          <div class="wrapper-3">
            <div class="pic"></div>
            <div class="img"></div>
            <div class="pic-2"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="box">
      <div class="wrapper-4" @click="goshop"><div class="img-2"></div></div>
      <span class="text-2">Details</span>
      <div class="section-5">
        <div class="section-6">
          <div class="img-3"></div>
          <div class="pic-3"></div>
          <div class="pic-4"></div>
        </div>
      </div>
    </div>
    <div class="pic-5"></div>
    <span class="text-3">Pet+ Subscription Plans</span
    ><span class="text-4">Subscribe to meet puppies & new friends</span>
    <div class="img-4">
      <div class="section-7">
        <span class="text-5">$5/mo for the first 3 months</span
        ><span class="text-6">撸狗，工作摸鱼的最小颗粒度</span
        ><span class="text-7">monthly plan</span>
        <div class="group-4"><span class="text-8">save 30%</span></div>
      </div>
      <div class="wrapper-5"><div class="img-5"></div></div>
    </div>
    <div class="pic-6">
      <div class="box-2">
        <span class="text-9">$3/month for one year</span
        ><span class="text-a">5折是坚持陪伴期许的浪漫</span
        ><span class="text-b">Annual plan</span>
        <div class="box-3"><span class="text-c">save 50%</span></div>
      </div>
      <div class="box-4"><div class="img-6"></div></div>
    </div>
    <div class="img-7">
      <div class="group-5">
        <span class="text-d">$100/month for lifetime access</span
        ><span class="text-e">陪伴，生活最长情的告白</span
        ><span class="text-f">Annual plan</span>
        <div class="section-8"><span class="text-10">save 80%</span></div>
      </div>
      <div class="box-5"><div class="pic-7"></div></div>
    </div>
    <div class="group-6"><span class="text-11">subscribe</span></div>
    <div class="wrapper-6"></div>
    <div class="pic-8"></div>
  </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';

const router = useRouter();

const goshop = () => {
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
.wrapper {
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
.group {
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
.section {
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
.group-2 {
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
.group-3 {
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
.section-2 {
  flex-shrink: 0;
  position: relative;
  width: 125px;
  height: 37px;
  background: #000000;
  z-index: 6;
  border-radius: 100px;
}
.wrapper-2 {
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
.section-3 {
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
.section-4 {
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
.wrapper-3 {
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
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/signal-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 11;
}
.img {
  flex-shrink: 0;
  position: relative;
  width: 17px;
  height: 11.834px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/wifi-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 12;
}
.pic-2 {
  flex-shrink: 0;
  position: relative;
  width: 27.401px;
  height: 13px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/battery-icon.svg)
    no-repeat center;
  background-size: cover;
  z-index: 13;
}
.box {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 94px;
  position: relative;
  width: 351px;
  height: 52px;
  margin: 11px 0 0 21px;
  z-index: 18;
}
.wrapper-4 {
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
  z-index: 19;
  border-radius: 25.5px;
}
.img-2 {
  flex-shrink: 0;
  position: relative;
  width: 11px;
  height: 15px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/back-arrow.svg)
    no-repeat center;
  background-size: cover;
  z-index: 20;
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
  z-index: 21;
}
.section-5 {
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
  z-index: 22;
  border-radius: 25.5px;
}
.section-6 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex-wrap: nowrap;
  flex-shrink: 0;
  gap: 3px;
  position: relative;
  width: 3px;
  z-index: 23;
}
.img-3 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/menu-dot-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 24;
  border-radius: 50%;
}
.pic-3 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/menu-dot-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 25;
  border-radius: 50%;
}
.pic-4 {
  align-self: stretch;
  flex-shrink: 0;
  position: relative;
  min-width: 0;
  height: 3px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/menu-dot-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 26;
  border-radius: 50%;
}
.pic-5 {
  position: relative;
  width: 206px;
  height: 75.484px;
  margin: 59px 0 0 109px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/logo.png)
    no-repeat center;
  background-size: cover;
  z-index: 27;
}
.text-3 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  width: 393px;
  height: 22px;
  margin: 47.516px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 16;
}
.text-4 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  position: relative;
  width: 287px;
  height: 15px;
  margin: 7px 0 0 53px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  opacity: 0.5;
  z-index: 17;
}
.img-4 {
  position: relative;
  width: 367.848px;
  height: 105.069px;
  margin: 17.825px 0 0 13.624px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/card-background-1.png)
    no-repeat center;
  background-size: cover;
  z-index: 29;
  border-radius: 17px;
}
.section-7 {
  position: absolute;
  height: 73.446px;
  top: 12.241px;
  right: 83.84px;
  left: 22.008px;
  font-size: 0px;
  z-index: 35;
}
.text-5 {
  display: block;
  position: relative;
  height: 19.382px;
  margin: 30.603px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 500;
  line-height: 19.364px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 31;
}
.text-6 {
  display: block;
  position: relative;
  height: 15.301px;
  margin: 8.16px 0 0 0;
  color: #989898;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  z-index: 32;
}
.text-7 {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22.442px;
  top: 0;
  left: calc(50% - 131px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 30;
}
.group-4 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 59.736px;
  height: 21.422px;
  top: 0.93px;
  left: 137.368px;
  padding: 4px 5px 4px 5px;
  background: linear-gradient(135deg, #fcefa9, #e5af4d);
  z-index: 35;
  border-radius: 3px;
}
.text-8 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 12px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 9.818181991577148px;
  font-weight: 600;
  line-height: 11.882px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 36;
}
.wrapper-5 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 48.208px;
  height: 46.924px;
  top: 29.583px;
  left: 301.824px;
  padding: 4px 4px 4px 4px;
  background: #252525;
  z-index: 33;
  border-radius: 23px;
}
.img-5 {
  flex-shrink: 0;
  position: relative;
  width: 37px;
  height: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/profile-avatar-1.svg)
    no-repeat center;
  background-size: cover;
  z-index: 34;
  overflow: hidden;
}
.pic-6 {
  position: relative;
  width: 367.848px;
  height: 105.069px;
  margin: 16.321px 0 0 13.624px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/card-background-2.png)
    no-repeat center;
  background-size: cover;
  z-index: 38;
  border-radius: 17px;
}
.box-2 {
  position: absolute;
  height: 73.902px;
  top: 11.785px;
  right: 83.84px;
  left: 22.008px;
  font-size: 0px;
  z-index: 44;
}
.text-9 {
  display: block;
  position: relative;
  height: 19.382px;
  margin: 31.059px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 500;
  line-height: 19.364px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 40;
}
.text-a {
  display: block;
  position: relative;
  height: 15.301px;
  margin: 8.16px 0 0 0;
  color: #989898;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  z-index: 41;
}
.text-b {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 23px;
  top: 0;
  left: calc(50% - 130.63px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 39;
}
.box-3 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 59.736px;
  height: 21.422px;
  top: 2px;
  left: 137.368px;
  padding: 4px 5px 4px 5px;
  background: linear-gradient(135deg, #fcefa9, #e5af4d);
  z-index: 44;
  border-radius: 3px;
}
.text-c {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 12px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 9.818181991577148px;
  font-weight: 600;
  line-height: 11.882px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 45;
}
.box-4 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 48.208px;
  height: 46.924px;
  top: 29.583px;
  left: 301.824px;
  padding: 4px 4px 4px 4px;
  background: #252525;
  z-index: 42;
  border-radius: 23px;
}
.img-6 {
  flex-shrink: 0;
  position: relative;
  width: 37px;
  height: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/profile-avatar-2.svg)
    no-repeat center;
  background-size: cover;
  z-index: 43;
  overflow: hidden;
}
.img-7 {
  position: relative;
  width: 367.848px;
  height: 105.069px;
  margin: 16.322px 0 0 13.624px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/card-background-3.png)
    no-repeat center;
  background-size: cover;
  z-index: 47;
  border-radius: 17px;
}
.group-5 {
  position: absolute;
  height: 73.446px;
  top: 12.241px;
  right: 83.84px;
  left: 22.008px;
  font-size: 0px;
  z-index: 53;
}
.text-d {
  display: block;
  position: relative;
  height: 19.382px;
  margin: 30.603px 0 0 0;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 16px;
  font-weight: 500;
  line-height: 19.364px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 49;
}
.text-e {
  display: block;
  position: relative;
  height: 15.301px;
  margin: 8.16px 0 0 0;
  color: #989898;
  font-family: Inter, var(--default-font-family);
  font-size: 12px;
  font-weight: 500;
  line-height: 14.523px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  letter-spacing: 0.48px;
  z-index: 50;
}
.text-f {
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  position: absolute;
  height: 22.442px;
  top: 0;
  left: calc(50% - 131px);
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 18px;
  font-weight: 500;
  line-height: 21.784px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 48;
}
.section-8 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 59.736px;
  height: 21.422px;
  top: 1.153px;
  left: 137.368px;
  padding: 4px 5px 4px 5px;
  background: linear-gradient(135deg, #fcefa9, #e5af4d);
  z-index: 53;
  border-radius: 3px;
}
.text-10 {
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  height: 12px;
  color: #000000;
  font-family: Inter, var(--default-font-family);
  font-size: 9.818181991577148px;
  font-weight: 600;
  line-height: 11.882px;
  text-align: left;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 54;
}
.box-5 {
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
  gap: 10px;
  position: absolute;
  width: 48.208px;
  height: 46.924px;
  top: 29.583px;
  left: 301.824px;
  padding: 4px 4px 4px 4px;
  background: #252525;
  z-index: 51;
  border-radius: 23px;
}
.pic-7 {
  flex-shrink: 0;
  position: relative;
  width: 37px;
  height: 37px;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/profile-avatar-3.svg)
    no-repeat center;
  background-size: cover;
  z-index: 52;
  overflow: hidden;
}
.group-6 {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  gap: 65px;
  position: relative;
  width: 350px;
  height: 60px;
  margin: 14.326px 0 0 22px;
  padding: 5px 6px 5px 6px;
  background: #ff5218;
  z-index: 56;
  border-radius: 29.5px;
}
.text-11 {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-shrink: 0;
  flex-basis: auto;
  position: relative;
  width: 99px;
  height: 25px;
  color: #ffffff;
  font-family: Inter, var(--default-font-family);
  font-size: 20.448429107666016px;
  font-weight: 500;
  line-height: 24.747px;
  text-align: center;
  text-transform: capitalize;
  white-space: nowrap;
  z-index: 57;
}
.wrapper-6 {
  position: relative;
  width: 134px;
  height: 5px;
  margin: 51px 0 0 130px;
  background: #000000;
  z-index: 15;
  border-radius: 100px;
}
.pic-8 {
  position: absolute;
  width: 393px;
  height: 43px;
  top: 671px;
  left: 0;
  background: url(https://static.codia.ai/custom_image/2025-04-07/113340/bottom-navigation.png)
    no-repeat center;
  background-size: cover;
  z-index: 55;
}

</style>

  