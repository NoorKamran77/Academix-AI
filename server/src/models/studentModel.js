import mongoose from "mongoose";
const studentSchema = new mongoose.Schema({

    userId:{
        type:mongoose.Schema.Types.ObjectId,
        ref:"User",
        required:true,
        unique:true
    },

    phone:String,

    college:String,

    semester:Number,

    bio:String,

    profileImage:String,
    
    institutionId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Institution",
    required: true
}

},{timestamps:true});

const Studentmodel = mongoose.model('Student', studentSchema);
export default Studentmodel;